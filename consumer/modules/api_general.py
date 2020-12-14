import random
import string
from django.conf import settings

def genUrl():
    url=''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])

    return url

def determineHost():
    return 'https://{}'.format(settings.ALLOWED_HOSTS[1]) if settings.DEBUG == False else 'http://{}:8000'.format(settings.ALLOWED_HOSTS[0])