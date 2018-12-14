from parkApp.base import *

ALLOWED_HOSTS = ['192.168.1.12']

BASE_DIR = '/home/deploy/parkApp/parkApp/'
STATIC_ROOT = "/home/deploy/parkApp/static"


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static/'),
]