from unittest import TestCase
from configuration import auth_token_yd
from yd_api import YDAPIclient


class TestYdAPI(TestCase):
    def test_creating_folder(self):
        yd_client = YDAPIclient(auth_token_yd)
        folder_name = 'Main'
        expected = 201
        actual = yd_client.creating_folder_in_yd(folder_name).status_code
        self.assertEqual(expected, actual)

    def test_creating_folder_exists(self):
        yd_client = YDAPIclient(auth_token_yd)
        folder_name = 'Main'
        expected = 409
        actual = yd_client.creating_folder_in_yd(folder_name).status_code
        self.assertEqual(expected, actual)

    def test_not_autorisation(self):
        auth_token = 'y0_AgAAAAAAqaP'
        yd_client = YDAPIclient(auth_token)
        folder_name = 'Main'
        expected = 401
        actual = yd_client.creating_folder_in_yd(folder_name).status_code
        self.assertEqual(expected, actual)