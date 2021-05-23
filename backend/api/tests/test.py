import json
from rest_framework import status
from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from messaging.serializers import *
from messaging.models import *
from datetime import datetime, timedelta
from django.contrib.auth.hashers import make_password
import random
import socket
import struct
from users.models import User
import json


def get_random_ip() -> str:
    return socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))


def get_token(client: APIClient, username: str, password: str) -> str:
    data = {
        'username': username,
        'password': password
    }

    response = client.post(reverse('api_token_auth'), data=json.dumps(data),
                           content_type='application/json')
    response_data = response.json()
    return f"Token {response_data.get('token')}"




class TestMessaging(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.users = User.objects.bulk_create(
            [
                User(
                    username=f'user{i}',
                    email=f'email{i}@mail.ru',
                    first_name=f'name{i}',
                    last_name=f'lastname{i}',
                    ip=get_random_ip(),
                    password=make_password('eldar123')
                )
                for i in range(3)]
        )

    def test_permission_when_create(self):
        data = {}
        response = self.client.post(reverse('messaging-list'), data=json.dumps(data),
                               content_type='application/json')

        assert response.status_code == 401
    
    def test_correct_input_when_create(self):
        token = get_token(self.client, self.users[0].username, 'eldar123')

        self.client = APIClient(REMOTE_ADDR=self.users[0].ip)
        self.client.credentials(HTTP_AUTHORIZATION=token)
        self.client.REMOTE_ADDR = self.users[0].ip

        data = {}
        response = self.client.post(reverse('messaging-list'), data=json.dumps(data),
                               content_type='application/json')
        response_data = response.json()

        assert response.status_code == 400
        assert 'title' in response_data
        assert 'body' in response_data

        data = {
            'title': 'title1',
            'body': 'body'
        }
        response = self.client.post(reverse('messaging-list'), data=json.dumps(data),
                               content_type='application/json')
        response_data = response.json()

        assert response.status_code == 201
    
    def test_mark_read(self):
        token = get_token(self.client, self.users[0].username, 'eldar123')

        self.client = APIClient(REMOTE_ADDR=self.users[0].ip)
        self.client.credentials(HTTP_AUTHORIZATION=token)
        self.client.REMOTE_ADDR = self.users[0].ip

        data = {
            'title': 'title1',
            'body': 'body'
        }
        response = self.client.post(reverse('messaging-list'), data=json.dumps(data),
                               content_type='application/json')

        msg_id = Message.objects.last().id

        response = self.client.post(reverse('messaging-mark-read', kwargs={'pk': msg_id}), pk=msg_id,
                               content_type='application/json')

        response_data = response.json()
        assert response.status_code == 200


        response = self.client.get(reverse('messaging-detail', kwargs={'pk': msg_id}), pk=msg_id,
                               content_type='application/json')

        response_data = response.json()
        assert response_data['id'] == msg_id
        assert response_data['title'] == 'title1'        
        assert response_data['body'] == 'body'        
        assert response_data['flag_read'] == True        
    

    # def test_throttling(self):
    #     token = get_token(self.client, self.users[0].username, 'eldar123')

    #     self.client = APIClient(REMOTE_ADDR=self.users[0].ip)
    #     self.client.credentials(HTTP_AUTHORIZATION=token)
    #     self.client.REMOTE_ADDR = self.users[0].ip

    #     for _ in range(11):
    #         data = {
    #             'title': 'title1',
    #             'body': 'body'
    #         }
    #         self.client.post(reverse('messaging-list'), data=json.dumps(data),
    #                             content_type='application/json')

    #     data = {
    #         'title': 'title1',
    #         'body': 'body'
    #     }
    #     response = self.client.post(reverse('messaging-list'), data=json.dumps(data),
    #                            content_type='application/json')

    #     print("RESPONSE STATUS", response.status_code, response.json())
    #     assert response.status_code == 429