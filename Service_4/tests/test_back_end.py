import unittest

from flask import url_for
from flask_testing import TestCase
from application import routes
from application import app

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
    def test_service4page_view(self):
        
        assert routes.name()=="james benson"