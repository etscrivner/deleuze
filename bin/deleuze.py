#!/usr/bin/env python
import os
import shutil
import sys

import jinja2


def copy_templated_file(base_dir, src, dest, context):
    """Copies the given template file after applying the given context.

    """
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(base_dir))
    template = env.get_template(src)

    result = template.render(**context)

    with open(os.path.join(base_dir, dest), 'w') as f:
        f.write(result)


def prompt(msg, default=None):
    """Displays a prompt with the given message and returns the given value or
    the default if nothing was entered.

    :param msg: The input prompt
    :type msg: basestring
    :param default: The default value

    """
    return raw_input(msg) or default


class Deleuze(object):

    KNOWN_COMMANDS = ('new',)

    def __init__(self, args):
        """Initialize the deleuze interface with the given arguments.

        :param args: The command-line arguments
        :type args: list

        """
        if len(args)  < 3:
            raise RuntimeError('Expected more command-line arguments')

        self.command = args[1]
        self.directory = args[2]

    def _prompt_for_answers(self, questions):
        """Takes a dictionary whose keys are considered command prompts and
        returns a new dictionary where the keys correspond to the entered
        values.

        :param questions: A dictionary whose keys are questions.
        :type questions: dict
        :return: A dictionary of answers for each of the questions.

        """
        results = {}

        for k, v in questions.iteritems():
            results[k] = prompt(k.capitalize().replace('_', ' ') + ': ', default='')

        return results

    def move(self, directory, source_path_parts, dest_path_parts):
        """Moves a file from the source to dest in the given directory.
        """
        shutil.move(
            os.path.join(self.directory, *source_path_parts),
            os.path.join(self.directory, *dest_path_parts)
        )

    def run(self):
        """Runs the command given to the project.

        """
        if self.command not in self.KNOWN_COMMANDS:
            raise RuntimeError('Unrecognized command {}'.format(self.command))

        print 'We need to get some initial project info'
        print 'Press Ctrl-C at any time to stop the process'
        print

        prompts = {
            'description': '',
            'author': '',
            'author_email': '',
            'url': '',
            'download_url': '',
            'package_name': '',
            'project_name': ''
        }

        answered_questions = self._prompt_for_answers(prompts)

        shutil.copytree('project-skeleton', self.directory)

        copy_templated_file(
            os.path.abspath(self.directory),
            'setup.jinja.py',
            'setup.py',
            answered_questions
        )

        os.unlink(os.path.join(self.directory, 'setup.jinja.py'))

        self.move(
            self.directory,
            ['NAME'],
            [answered_questions['package_name']]
        )

        self.move(
            self.directory,
            ['bin', 'NAME.py'],
            ['bin', '{}.py'.format(answered_questions['package_name'])]
        )

        self.move(
            self.directory,
            ['tests', 'test_NAME.py'],
            ['tests', 'test_{}.py'.format(answered_questions['package_name'])]
        )


if __name__ == '__main__':
    Deleuze(sys.argv).run()
