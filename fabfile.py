from fabric.api import *

env.hosts = ['kaylee.robgolding.com']

def deploy():
	run("cd myuni && hg pull -u")
