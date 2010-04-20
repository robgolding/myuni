import os

SERVE_MEDIA = True
PATH = os.path.abspath(os.path.dirname(__file__))

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = os.path.join(PATH, 'dev.db')
