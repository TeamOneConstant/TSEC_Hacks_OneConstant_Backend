import os
import datetime
from django.db import transaction
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from accounts.models import *
from accounts.serializers import *
from backend import settings

import facebook as fb

from integrations.helpers import upload_media
from integrations.models import *


# Create your views here.



fb_access_token = "EAAFRv3NToBgBO6GBVZAaXbrc3SYvwAfkeS3rx9BeQivhJavWxAwDg57XyO2E3ftxZBWoZCcFOPFbWMFqPqoZAkc4ocyBcPwbfyQmVXI4AcTycycVb8WH6hmKUwjZC60tgRsea4NpAVR7OAURHsSxARPHZCgVtk9u0sKYO41BrDqSWd7tzPtTFESqReGNEeZAq1QOwPfwNMZD"
print("fb_access_token :: ", fb_access_token)
fb_obj = fb.GraphAPI(fb_access_token)




class FacebookIntegrationAPI(APIView):

    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    @transaction.atomic
    def post(self, request):

        try:
            rd = request.data
            user = request.user

            if rd['platform'] == "facebook":
                res = {}
                if rd['post_type'] == "text":
                    res = fb_obj.put_object("me", "feed", message=rd['text'])
                    photo = None

                elif rd['post_type'] == "photo":
                    res = fb_obj.put_photo(request.FILES['photo'], message=rd['text'] if rd.get('text', None) is not None else "")
                    photo = upload_media(request, platform="facebook")

                print("res :: ", res)
            
            else:
                return Response({"success": False, "message": "Unknown platform!"})

            
            new_ph = PostHistory.objects.create(user=user, platform=rd['platform'], photo=photo, text=rd['text'],
                                                post_type=rd['post_type'], response=res)

            return Response({"success": True, "message": "Post created successfully!"})

        except Exception as err:
            print(err)
            return Response({"success": False, "message": "Something went wrong!"})





