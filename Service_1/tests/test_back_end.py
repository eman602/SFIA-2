import unittest

from flask import url_for
from flask_testing import TestCase

from application import app
from application.models import Names
from os import getenv

class TestBase(TestCase):

    def create_app(self):

        # pass in configurations for test database
        config_name = 'testing'
        
        return app

    def setUp(self):
        """
        Will be called before every test
        """
        # ensure there is no data in the test database when the test starts
        

        # create test admin user
        

    def tearDown(self):
        """
        Will be called after every test
        """

        

class TestViews(TestBase):
    def test_homepage_view(self):
        response=self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
