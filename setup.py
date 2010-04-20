import os
from setuptools import setup, find_packages

def read(fname):
	return open(os.path.join(os.path.dirname(__file__), fname)).read()

def fullsplit(path, result=None):
	"""
	Split a pathname into components (the opposite of os.path.join) in a
	platform-neutral way.
	"""
	if result is None:
		result = []
	head, tail = os.path.split(path)
	if head == '':
		return [tail] + result
	if head == path:
		return result
	return fullsplit(head, [tail] + result)

# Compile the list of packages available, because distutils doesn't have
# an easy way to do this.import myuni
packages, data_files = [], []
root_dir = os.path.dirname(__file__)
myuni_dir = os.path.join(root_dir, 'myuni')
pieces = fullsplit(root_dir)
if pieces[-1] == '':
    len_root_dir = len(pieces) - 1
else:
    len_root_dir = len(pieces)

for dirpath, dirnames, filenames in os.walk(myuni_dir):
	# Ignore dirnames that start with '.'
	for i, dirname in enumerate(dirnames):
		if dirname.startswith('.'): del dirnames[i]
	if '__init__.py' in filenames:
		packages.append('.'.join(fullsplit(dirpath)[len_root_dir:]))
	elif filenames:
		data_files.append([dirpath, [os.path.join(dirpath, f) for f in filenames]])

version = __import__('myuni').get_version()
if u'hg' in version:
	version = ' '.join(version.split(' ')[:-1])

setup(
	name = "myuni",
	version = version.replace(' ', '-'),
	packages = packages,
	data_files = data_files,
	author = "Rob Golding, Robert S. K. Miles, Marcus Whybrow",
	description = "A portal-style web application for Universities.",
	long_description=read('README.txt'),
	license = "GPL",
	keywords = "django university student",
	classifiers=[
		'Framework :: Django',
		'Programming Language :: Python',
		'Operating System :: OS Independent',
		'Environment :: Web Environment',
	],
	url = "http://bitbucket.org/robgolding63/myuni",
)
