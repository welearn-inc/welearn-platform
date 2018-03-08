from WeLearn.settings.base import *

# Override base.py settings here

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'AAs65snz9+3vnhjmr3hijb0u@&w68t#5_e8s9-lbfhv-')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1','localhost','welearn-platform.herokuapp.com','api.welearn.school']

# Update database configuration with $DATABASE_URL.
import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
