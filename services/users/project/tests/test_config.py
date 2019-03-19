import os
import unittest

from flask import current_app
from flask_testing import TestCase
from project import create_app


class TestDevelopmentConfig(TestCase):

    def create_app(self):
        app = create_app()
        app.config.from_object('project.config.DevelopmentConfig')
        return app

    def test_app_is_development(self):
        self.assertTrue(self.app.config['SECRET_KEY'] == 'my_precious')
        self.assertFalse(current_app is None)
        self.assertTrue(
            self.app.config['SQLALCHEMY_DATABASE_URI'] ==
            os.environ.get('DATABASE_URL')
        )


class TestTestingConfig(TestCase):

    def create_app(self):
        app = create_app()
        app.config.from_object('project.config.TestingConfig')
        return app

    def test_app_is_testing(self):
        self.assertTrue(self.app.config['SECRET_KEY'] == 'my_precious')
        self.assertTrue(self.app.config['TESTING'])
        self.assertFalse(self.app.config['PRESERVE_CONTEXT_ON_EXCEPTION'])
        self.assertTrue(
            self.app.config['SQLALCHEMY_DATABASE_URI'] ==
            os.getenv('DATABASE_TEST_URL')
        )


class TestProductionConfig(TestCase):
    def create_app(self):
        app = create_app()
        app.config.from_object('project.config.ProductionConfig')
        return app

    def test_app_is_production(self):
        self.assertTrue(self.app.config['SECRET_KEY'] == 'my_precious')
        self.assertFalse(self.app.config['TESTING'])


if __name__ == '__main__':
    unittest.main()
