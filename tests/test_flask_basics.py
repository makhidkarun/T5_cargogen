'''test_flask_basics.py'''

import unittest
from flask import current_app
from app import create_app


class BasicsTestCase(unittest.TestCase):
    '''Flask basic tests'''
    def setUp(self):
        '''Test Flask app setup'''
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        '''Test Flask app teardown'''
        self.app_context.pop()

    def test_app_exists(self):
        '''Test Flask app exists'''
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        '''Test Flask app environment is TESTING'''
        self.assertTrue(current_app.config['TESTING'])
