import unittest
from App import my_app
import os
import json
import pytest
import datetime


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.app = my_app
        self.client = self.app.test_client()

        target_time = datetime.datetime.now() + datetime.timedelta(days=7)
        target_time = target_time.replace(microsecond=0)
        today_now = datetime.datetime.now()

        self.meetup1 = {
            "topic": "My first meetup",
            "description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has",
            "images": ["/home/zonecc/pictures/img1.png", "/home/zonecc/picturesimg2/png"],
            "location": "Home",
            "happenOn": target_time.strftime("%D %H:%M %p"),
            "tags": ["#At home", "#coding", "#enjoy"]
        }

        self.meetup1created = {
            "id": 1,
            "createOn": today_now.strftime("%d %h %Y"),
            "topic": "My first meetup",
            "description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has",
            "images": ["/home/zonecc/pictures/img1.png", "/home/zonecc/picturesimg2/png"],
            "location": "Home",
            "happenOn": target_time.strftime("%D %H:%M %p"),
            "tags": ["#At home", "#coding", "#enjoy"]
        }

        self.meetup2 = {
            "description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has",
            "images": ["/home/zonecc/pictures/img1.png", "/home/zonecc/picturesimg2/png"],
            "location": "Home",
            "happenOn": target_time.strftime("%D %H:%M %p"),
            "tags": ["#At home", "#coding", "#enjoy"]
        }

    def tearDown(self):
        pass


class TestMeetup(BaseTest):
    def test_created_meetup_success(self):
        response = self.client.post(
            '/api/v1/meetups', data=json.dumps(self.meetup1), content_type="application/json")
        self.assertEqual(response.status_code, 201)

    def test_created_meetup_fail(self):
        response = self.client.post(
            '/api/v1/meetups', data=json.dumps(self.meetup2), content_type="application/json")
        self.assertEqual(response.status_code, 201)
