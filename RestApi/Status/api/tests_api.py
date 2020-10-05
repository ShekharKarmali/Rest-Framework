import os
import shutil
import tempfile

from PIL import Image

from django.urls import reverse
from rest_framework import status
from rest_framework.reverse import reverse as api_reverse
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from django.conf import settings

from rest_framework_jwt.settings import api_settings

from Status.models import Status

jwt_payload_handler             = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler              = api_settings.JWT_ENCODE_HANDLER

User = get_user_model()

class StatusAPITestCase(APITestCase):
    def setUp(self):
        user=User.objects.create(username='testcfeuser',email='hellocfe@gmail.com')
        user.set_password('yeahcfe')
        user.save()
        Status_obj=Status.objects.create(user=user,content='hello there')

    def test_statuses(self):
        self.assertEqual(Status.objects.count(),1)
    

    def status_user_token(self):
        auth_url=api_reverse('api-auth:login')
        auth_data={
            'username':'testcfeuser',
            'password':'yeahcfe'
        }
        auth_response=self.client.post(auth_url,auth_data,format='json')
        token=auth_response.data.get("token",None)
        if token is not None:
            self.client.credentials(HTTP_AUTHORIZATION='JWT' + token)
        

    def create_item(self):
        self.status_user_token()
        url=api_reverse('api-status:list')
        data={
            'content':"some cool test content"
        }
        response=self.client.post(url,data,format='json')
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        self.asserEqual(Status.objects.count(),2)
        return response.data

    def test_empty_create_item(self):
        self.status_user_token()
        url = api_reverse('api-status:list')
        data = {
            'content': None,
            'image': None
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        return response.data