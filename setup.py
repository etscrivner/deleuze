try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

config = {
    'description': 'Simple python project creation tool - inspired by Leiningen.',
    'author': 'Eric Scrivner',
    'url': 'https://github.com/etscrivner/deleuze',
    'download_url': 'https://github.com/etscrivner/deleuze',
    'author_email': 'eric.t.scrivner@gmail.com',
    'version': '0.9',
    'install_requires': ['Jinja2'],
    'license': 'BSD',
    'keywords': 'project, project creation, scaffolding, scaffold',
    'include_package_data': True,
    'scripts': [],
    'name': 'deleuze',
    'packages': find_packages(),
    'entry_points': {
        'console_scripts': [
            'deleuze = deleuze.tool:main'
        ]
    }
}

setup(**config)
