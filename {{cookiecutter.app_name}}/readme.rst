{{cookiecutter.project_name}}
=============================

Brief description of project here.

Installation
------------

1. Install from PIP::

    pip install {{cookiecutter.app_name}}

2. Enable for a ticket folder::

    jirafs plugins --enable={{cookiecutter.plugin_name}}

Note that you can globally enable this (or any) plugin by adding the
``--global`` flag to the above command::

    jirafs plugins --global --enable={{cookiecutter.plugin_name}}

