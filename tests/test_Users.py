import unittest
from App import my_app
import os
import json
import pytest


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.app = my_app
        self.client = self.app.test_client()

        self.usercreate1 = {
            "firstName": "Trevor",
            "lastName": "Kurland",
            "otherName": "Burudi",
            "userName": "trevor",
            "email": "trevbk@gmail.com",
            "phone": "+254712345678",
            "password": "$$22BBkk",
            "confirmPassword": "$$22BBkk"
        }

        self.userlogin1 = {
            "username": "trevor",
            "password": "$22BBkk"
        }

        self.userlogin2 = {
            "email": "trevbk@gmail.com",
            "password": "$22BBkk"
        }

        self.userlogin3 = {
            "username": "zonec",
            "password": "$22BBkk"
        }

        self.userlogin4 = {
            "email": "trevbkbk@gmail.com",
            "password": "$22BBkk"
        }

    def tearDown(self):
        pass


class TestUsers(BaseTest):
    def test_signup_successful(self):
        response = self.client.post(
            'api/v1/signup', data=json.dumps(self.usercreate1), content_type="application/json")
        self.assertEqual(response.status_code, 201)

    def test_login_username_success(self):
        response = self.client.post(
            'api/v1/login', data=json.dumps(self.userlogin1), content_type="application/json")
        self.assertEqual(response.status_code, 200)

    def test_login_email_success(self):
        response = self.client.post(
            'api/v1/login', data=json.dumps(self.userlogin1), content_type="application/json")
        self.assertEqual(response.status_code, 200)

    def test_login_email_fail_username(self):
        response = self.client.post(
            'api/v1/login', data=json.dumps(self.userlogin3), content_type="application/json")
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 401)
        self.assertEqual("username not found", result["error"])

    def test_login_email_fail_email(self):
        response = self.client.post(
            'api/v1/login', data=json.dumps(self.userlogin4), content_type="application/json")
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 401)
        self.assertEqual("email not found", result["error"])


if __name__ == "__main__":
    unittest.main()
