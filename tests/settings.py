from project.settings import *

DATABASES = {
    'default': {
        'NAME': ':memory:',  # Usa un database in-memory durante i test
        'ENGINE': 'django.db.backends.sqlite3',  # Usa SQLite per i test
    }
}
