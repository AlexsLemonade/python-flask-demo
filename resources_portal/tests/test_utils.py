import unittest

from resources_portal import resources_portal
from resources_portal.db import db


class ApiTestCase(unittest.TestCase):
    def setUp(self):
        self.app = resources_portal.create_app()

        # Ensure that the tests were run with the correct environment.
        assert self.app.config["TESTING"]

        self.client = self.app.test_client()

        with self.app.app_context():
            db.drop_all()
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()
