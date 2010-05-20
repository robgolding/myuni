import os

from default_settings import *

PATH = os.path.abspath(os.path.dirname(__file__))

DATABASES = {
	'default': {
		'ENGINE': 'sqlite3',
		'NAME': os.path.join(PATH, 'test.db'),
	}
}

import random, string

SECRET_KEY = ''.join([random.choice(string.letters+string.digits) for i in range(30))]
