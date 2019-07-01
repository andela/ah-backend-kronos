import os

import facebook
from google.auth.transport import requests
from google.oauth2 import id_token
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from authors.apps.authentication.renderers import UserJSONRenderer

from .exceptions import SocialAuthenticationFailed
from .login_register import login_or_register_social_user


class FacebookAuthAPIView(CreateAPIView):
    renderer_classes = (UserJSONRenderer,)

    def post(self, request):
        facebook_token = request.data.get('user', {})
        access_token = facebook_token.get("access_token", {})
        try:
            graph = facebook.GraphAPI(access_token=access_token)
            facebook_user = graph.get_object(id='me', fields='email, name')
        except:
            raise SocialAuthenticationFailed
        response =  login_or_register_social_user(facebook_user)
        return Response(response, status=status.HTTP_200_OK)

class GoogleAuthAPIView(CreateAPIView):
    renderer_classes = (UserJSONRenderer,)

    def post(self, request):
        google_token = request.data.get('user', {})
        access_token = google_token.get("access_token", {})
        try:
            google_user = id_token.verify_oauth2_token(
                access_token, requests.Request())
        except:
            raise SocialAuthenticationFailed
        response = login_or_register_social_user(google_user)
        return Response(response, status=status.HTTP_200_OK)
