from resources_portal.tests.test_utils import ApiTestCase


class UserTestCase(ApiTestCase):
    def test_list_empty(self):
        user_list = self.client.get("/users")
        self.assertEqual([], user_list.get_json())
