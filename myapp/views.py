from django.shortcuts import render
from django.utils import timezone
from django.db.models import Q
import calendar
from datetime import datetime as dtt,time,date,timedelta
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from squarebackend.responsecode import display_response

from .models import *
from .serializers import *
from .utils import *
from .auth import *

#--------LoginUser API--------
class LoginUser(APIView):

    authentication_classes=[]
    permission_classes=[]

    def post(self,request,fromat=None):

        data=request.data
        
        public_key=data.get("public_key",None)
        password=data.get("password",None)

        #validating the mobile number
        if public_key in ["",None] or password in ["",None]:
            return display_response(
                msg="FAIL",
                err="Please provided user data(mobile number, email, password)",
                body=None,
                statuscode=status.HTTP_406_NOT_ACCEPTABLE
            )


        #gets the userinstance in case of old user or creates a new user instance        
        user_instance=User.objects.filter(Q(phone=public_key) | Q(email=public_key)).first()
        if user_instance is None:
            return display_response(
                msg="FAIL",
                err="User does not exist.Try signup",
                body=None,
                statuscode=status.HTTP_406_NOT_ACCEPTABLE
            )
        
        #validating the password
        if user_instance.password!=password:
            return display_response(
                msg="FAIL",
                err="Incorrect password",
                body=None,
                statuscode=status.HTTP_406_NOT_ACCEPTABLE
            )
    
        #generating the token
        token=generate_token({
                        "id":user_instance.id
                                })
        
        #returning the response
        return display_response(
            msg="SUCCESS",
            err=None,
            body={
                "token":token,
                "user":UserSerializer(user_instance,context={"request":request}).data
            },
            statuscode=status.HTTP_200_OK
        )


