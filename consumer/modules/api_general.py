import random
import string
import pytz
from django.conf import settings

def genUrl():
    url=''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])

    return url

def determineHost():
    return 'https://{}'.format(settings.ALLOWED_HOSTS[1]) if settings.DEBUG == False else 'http://{}:8000'.format(settings.ALLOWED_HOSTS[0])

def genDateTimeString(dateObj):
    naiTimeZone=pytz.timezone("Africa/Nairobi")
    naiTime=dateObj.astimezone(naiTimeZone)
    dateString=naiTime.strftime("%a, %d %b %Y at %I:%M:%S%p")

    return dateString