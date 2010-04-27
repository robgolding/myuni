.. _installation:

================
Installing MyUni
================

We're going to use all the hottest Python tools to set up a nice environment.
Here we go!


Requirements
------------

To get started, you'll need and internet connection and Python 2.6.


Use the Source
~~~~~~~~~~~~~~

Grab MyUni from bitbucket with ::

    hg clone http://bitbucket.org/robgolding63/myuni


virtualenv
----------

`virtualenv <http://pypi.python.org/pypi/virtualenv>`_ is a tool to create
isolated Python environments.  We're going to be installing a bunch of packages,
but we don't want your system littered with all these things you only need for
MyUni. Some other piece of software might want an older version than MyUni
wants, which can create quite a mess.  ::

    easy_install virtualenv

virtualenv is the only package I install system-wide.  Everything else goes in a
virtual environment.


virtualenvwrapper
-----------------

`virtualenvwrapper <http://www.doughellmann.com/docs/virtualenvwrapper/>`_
complements virtualenv by installing some shell functions that make environment
management smoother.  ::

    easy_install virtualenvwrapper

Then put these lines in your ``~/.bashrc``::

    export WORKON_HOME=$HOME/.virtualenvs
    source $HOME/.virtualenvwrapper

``exec bash`` and you're set.


Getting Packages
----------------

Now we're ready to go, so create an environment for MyUni::

    mkvirtualenv --no-site-packages myuni

That creates a clean environment named myuni and (for convenience) initializes
the environment.  You can get out of the environment by restarting your shell or
calling ``deactivate``.

To get back into the MyUni environment later, type::

    workon myuni

If you keep your Python binary in a special place (i.e. you don't want to use
the system Python), pass the path to mkvirtualenv with ``--python``::

    mkvirtualenv --python=/usr/local/bin/python2.6 --no-site-packages myuni


pip
~~~

We're going to use pip to install Python packages from `pypi
<http://pypi.python.org/pypi>`_. ::

    easy_install pip

Since we're in our isolated environment, pip was only installed locally, not
system-wide.

MyUni uses a requirements file to tell pip what to install.  Get everything
you need by running ::

    pip install -r requirements.txt

from the root of your MyUni checkout.


Settings
--------

Most of MyUni is configured in ``settings.py``, but it's incomplete since we
don't want to put database passwords into version control.  Local settings
are stored in ``local_settings.py``, which is imported into the main settings
file at the end.

The local settings template is included in the project directory as
``local_settings.py.template``, so to start using it, just copy it over: ::

    cp local_settings.py.template local_settings.py

The Mercurial repository is setup to ignore this file, so don't worry about
that.

The local settings template overrides the database parameters from
``settings.py`` and then extends ``INSTALLED_APPS`` and ``MIDDLEWARE_CLASSES``
to include the `Django Debug Toolbar
<http://github.com/robhudson/django-debug-toolbar>`_.  It's awesome, and I
recommend you install it to take full advantage.


Database
--------

To create the development database, run ::

    ./manage.py syncdb

to get the auth and admin tables from Django, and create a superuser for
yourself.


Fin
---

Everything's good to go now so start up the development server. ::

    python manage.py runserver
