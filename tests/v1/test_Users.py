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
        self.usercreate2 = {
            "firstName": "",
            "lastName": "Kurland",
            "otherName": "Burudi",
            "userName": "trevor",
            "email": "trevbk@gmail.com",
            "phone": "+254712345678",
            "password": "$$22BBkk",
            "confirmPassword": "$$22BBkk"
        }
        self.usercreate3 = {
            "firstName": "Trevor",
            "lastName": "",
            "otherName": "Burudi",
            "userName": "trevor",
            "email": "trevbk@gmail.com",
            "phone": "+254712345678",
            "password": "$$22BBkk",
            "confirmPassword": "$$22BBkk"
        }
        self.usercreate4 = {
            "firstName": "Trevor",
            "lastName": "Kurland",
            "otherName": "Burudi",
            "userName": "trevor",
            "email": "",
            "phone": "+254712345678",
            "password": "$$22BBkk",
            "confirmPassword": "$$22BBkk"
        }
        self.usercreate5 = {
            "firstName": "Trevor",
            "lastName": "Kurland",
            "otherName": "Burudi",
            "userName": "trevor",
            "email": "hhhhh@mm.com",
            "phone": "+254712345678",
            "password": "",
            "confirmPassword": "$$22BBkk"
        }
        self.usercreate6 = {
            "firstName": "Trevor",
            "lastName": "Kurland",
            "otherName": "Burudi",
            "userName": "trevor",
            "email": "abc@abc.com",
            "phone": "+254712345678",
            "password": "$$22BBkk",
            "confirmPassword": ""
        }

        self.usercreate7 = {
            "firstName": "Trevor",
            "userName": "trevor",
            "email": "abc@abc.com",
            "phone": "+254712345678",
            "password": "$$22BBkk",
            "confirmPassword": ""
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

        self.nodata = {}

    def tearDown(self):
        pass


class TestUsers(BaseTest):
    def test_signup_successful(self):
        response = self.client.post(
            'api/v1/signup', data=json.dumps(self.usercreate1), content_type="application/json")
        self.assertEqual(response.status_code, 201)

    def test_signup_fail_no_data(self):
        response = self.client.post(
            'api/v1/signup', data=json.dumps(self.nodata), content_type="application/json")
        self.assertEqual(response.status_code, 204)

    def test_signup_fail_missing_key_field(self):
        response = self.client.post(
            'api/v1/signup', data=json.dumps(self.usercreate7), content_type="application/json")
        self.assertEqual(response.status_code, 400)

    def test_signup_fail_missing_phone(self):
        response = self.client.post(
            'api/v1/signup', data=json.dumps(self.usercreate2), content_type="application/json")
        self.assertEqual(response.status_code, 422)

    def test_signup_fail_missing_f_name(self):
        response = self.client.post(
            'api/v1/signup', data=json.dumps(self.usercreate3), content_type="application/json")
        self.assertEqual(response.status_code, 422)

    def test_signup_fail_missing_l_name(self):
        response = self.client.post(
            'api/v1/signup', data=json.dumps(self.usercreate4), content_type="application/json")
        self.assertEqual(response.status_code, 422)

    def test_signup_fail_missing_email(self):
        response = self.client.post(
            'api/v1/signup', data=json.dumps(self.usercreate5), content_type="application/json")
        self.assertEqual(response.status_code, 422)

    def test_signup_fail_missing_password(self):
        response = self.client.post(
            'api/v1/signup', data=json.dumps(self.usercreate6), content_type="application/json")
        self.assertEqual(response.status_code, 422)

    def test_signup_fail_missing_c_password(self):
        response = self.client.post(
            'api/v1/signup', data=json.dumps(self.usercreate2), content_type="application/json")
        self.assertEqual(response.status_code, 422)

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
