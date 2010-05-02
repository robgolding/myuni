from fabric.api import *

"""
Base configuration
"""
env.project_name = 'myuni'
env.apps = ['modules']
env.database_host = 'book'
env.database_name = env.project_name
env.database_user = env.project_name
env.database_password = 'hg267ds0'
env.path = '/home/django/%(project_name)s' % env
env.env_path = '%(path)s/env' % env
env.repo_path = '%(path)s/repository' % env
env.repo_url = 'https://robgolding63@bitbucket.org/robgolding63/myuni'
env.production_domain = 'robgolding.com'
env.staging_domain = 'kaylee.robgolding.com'

"""
Environments
"""
def production():
    """
    Work on production environment
    """
    env.settings = 'production'
    env.hosts = ['%(production_domain)s' % env]

def staging():
    """
    Work on staging environment
    """
    env.settings = 'staging'
    env.hosts = ['%(staging_domain)s' % env]

"""
Commands - setup
"""
def setup():
    """
    Setup a fresh virtualenv, install everything we need, and fire up the database.
    """
    require('settings', provided_by=[production, staging])

    setup_directories()
    setup_virtualenv()
    clone_repo()
    pull_update()
    install_requirements()
    destroy_database()
    create_database()
    syncdb()

def setup_directories():
    """
    Create directories necessary for deployment.
    """
    run('mkdir -p %(path)s' % env)
    run('mkdir -p %(env_path)s' % env)

def setup_virtualenv():
    """
    Setup a fresh virtualenv.
    """
    run('virtualenv --no-site-packages %(env_path)s;' % env)
    run('source %(env_path)s/bin/activate; easy_install -U setuptools; easy_install pip;' % env)

def clone_repo():
    """
    Clone the repository.
    """
    run('hg clone %(repo_url)s %(repo_path)s' % env)

def pull_update():
    """
    Pull the latest changesets into the local repo.
    """
    run('cd %(repo_path)s; hg pull -u' % env)

def install_requirements():
    """
    Install the required packages using pip.
    """
    run('source %(env_path)s/bin/activate; pip install -E %(env_path)s -r %(repo_path)s/requirements.txt' % env)

"""
Commands - deployment
"""
def deploy():
    """
    Deploy the latest version of the site to the server and restart Apache.
    """
    require('settings', provided_by=[production, staging])
    
    pull_update()
    install_requirements()
    reset_apps()
    syncdb()
    remake_docs()
    reboot()

def remake_docs():
	"""
    Rebuild the documentation on the server.
    """
	run("source %(env_path)s/bin/activate; cd %(repo_path)s/docs; make" % env)

def maintenance_up():
    """
    Install the Apache maintenance configuration.
    """
    pass

def maintenance_down():
    """
    Reinstall the normal site configuration.
    """
    pass

def reboot():
    """
    Restart the Apache server.
    """
    sudo('/etc/init.d/apache2 restart')

"""
Commands - data
"""
def create_database():
	"""
    Create the SQL database.
    """
	require('settings', provided_by=[production, staging])
	
	run('mysql -h%(database_host)s -u%(database_user)s -p%(database_password)s -e"CREATE DATABASE %(database_name)s;"' % env)

def destroy_database():
	"""
    Drop the SQL database.
    """
	require('settings', provided_by=[production, staging])
	
	run('mysql -h%(database_host)s -u%(database_user)s -p%(database_password)s -e"DROP DATABASE %(database_name)s;"' % env)

def reset_apps():
	"""
    Perform Django's `reset' command for all listed apps.
    """
	require('settings', provided_by=[production, staging])
	
	env.apps_s = ' '.join(env.apps)
	run('source %(env_path)s/bin/activate; cd %(repo_path)s; cd %(project_name)s; python manage.py reset %(apps_s)s --noinput' % env)

def syncdb():
    """
    Perform Django's `syncdb' command.
    """
    require('settings', provided_by=[production, staging])

    run("cd %(repo_path)s; cd %(project_name)s; python manage.py syncdb --noinput" % env)
