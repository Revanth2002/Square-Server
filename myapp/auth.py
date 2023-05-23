from django.conf import settings
from django.utils import timezone
from datetime import timedelta
from django.utils.translation import gettext_lazy as _

from .models import *
import jwt

from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
import hashlib 
    
def generate_token(payload):
    """
        function to generate authentication token of a user
    """
    dt=timezone.now()+timedelta(days=60)

    payload["exp"]=dt.timestamp()

    return jwt.encode(payload,settings.SECRET_KEY,algorithm="HS256")


def get_request_header(request):
	header=request.META.get('HTTP_AUTHORIZATION','')
	
	return header

