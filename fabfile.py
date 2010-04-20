from fabric.api import *

env.hosts = ['kaylee.robgolding.com']

def deploy():
	local("hg push staging")
