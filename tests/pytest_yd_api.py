import pytest
from configuration import auth_token_yd
from yd_api import YDAPIclient


@pytest.mark.parametrize(
    'auth_token, expected, folder_name',
    (
        [auth_token_yd, 201, 'Main'],
        [auth_token_yd, 409, 'Main'],
        ['y0_AgAAAAAAqaP', 401, 'Main']
    )
)
def test_creating_folder(auth_token, expected, folder_name):
    yd_client = YDAPIclient(auth_token)
    actual = yd_client.creating_folder_in_yd(folder_name).status_code
    assert expected == actual
