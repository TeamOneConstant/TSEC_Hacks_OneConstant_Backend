import datetime
from django.contrib.auth.models import auth
from django.db import transaction
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from accounts.models import *
from accounts.serializers import *
# Create your views here.




class UserLogin(APIView):

    # permission_classes = [IsAuthenticated]
    # authentication_classes = [JWTAuthentication]
    permission_classes = []
    authentication_classes = []

    @transaction.atomic
    def post(self, request):

        try:
            rd = request.data
            user = CustomUser.objects.filter(email=rd['email']).first()
            if user == None:

                user = CustomUser.objects.create(email=rd['email'], username=rd['email'], full_name=rd['fname'], 
                                                    is_verified=True, email_verified_at=datetime.datetime.now())
            
            token = RefreshToken.for_user(user)
            data = CustomUserSerializer(user).data

            return Response({"success": True, "message": "User login successful!", "data": data,
                             "authToken": {
                                'type': 'Bearer',
                                'access': str(token.access_token),
                                'refresh': str(token),
                            }})

        except Exception as err:
            print(err)
            return Response({"success": False, "message": "Something went wrong!",})




