import os
from setuptools import setup, find_packages
import uuid

from {{cookiecutter.app_name}} import __version__ as version_string


requirements_path = os.path.join(
    os.path.dirname(__file__),
    'requirements.txt',
)
try:
    from pip.req import parse_requirements
    requirements = [
        str(req.req) for req in parse_requirements(
            requirements_path,
            session=uuid.uuid1()
        )
    ]
except (ImportError, AttributeError, ValueError, TypeError):
    requirements = []
    with open(requirements_path, 'r') as in_:
        requirements = [
            req for req in in_.readlines()
            if not req.startswith('-')
            and not req.startswith('#')
        ]


setup(
    name='{{cookiecutter.app_name}}',
    version=version_string,
    url='https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.repo_name}}',
    description="{{cookiecutter.project_short_description}}"
    author='{{cookiecutter.full_name}}',
    author_email='{{cookiecutter.email}}',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
    ],
    install_requires=requirements,
    include_package_data=True,
    packages=find_packages(),
    entry_points={
        '{{cookiecutter.app_name}}': [
            '{{cookiecutter.plugin_name}} = {{cookiecutter.app_name}}.plugin:Plugin',
        ]
    },
)
