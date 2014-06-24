try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': '{{ description }}',
    'author': '{{ author }}',
    'url': '{{ url }}',
    'download_url': '{{ download_url }}',
    'author_email': '{{ author_email }}',
    'version': '0.1',
    'install_requires': [''],
    'packages': ['{{ package_name }}'],
    'scripts': [],
    'name': '{{ project_name }}'
}

setup(**config)
