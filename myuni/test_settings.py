import os

from default_settings import *

PATH = os.path.abspath(os.path.dirname(__file__))

DATABASES = {
	'default': {
		'ENGINE': 'sqlite3',
		'NAME': os.path.join(PATH, 'test.db'),
	}
}
