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
            "userlog": "zonecc",
            "password": "$22BBkk"
        }

        self.userlogin2 = {
            "userlog": "m_m_m_mm@gmail.com",
            "password": "$22BBkk"
        }

        self.userlogin3 = {
            "userlog": "zonec",
            "password": "$22BBkk"
        }

        self.userlogin4 = {
            "userlog": "trevbkbk@gmail.com",
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
        self.assertEqual(response.status_code, 401)

    def test_login_email_fail_email(self):
        response = self.client.post(
            'api/v1/login', data=json.dumps(self.userlogin4), content_type="application/json")
        self.assertEqual(response.status_code, 401)


if __name__ == "__main__":
    unittest.main()
