## "https://my-json-server.typicode.com/typicode/demo/posts"

import requests
from configuration import SERVICE_URL
from enums.global_enums import GlobalErrorMessages


def test_equal():
    assert 1 == 1, "Not equal"


def test_not_equal():
    assert 1 != 2, "Numbers are equal"


def test_getting_post():
    response = requests.get(url=SERVICE_URL)
    received_post = response.json()
    print(received_post)

    assert response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value
    assert len(received_post) == 3, GlobalErrorMessages.WRONG_ELEMENT_COUNT.value





