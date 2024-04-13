import requests
import pytest
import json
from http import HTTPStatus

"""Rest API for https://petstore.swagger.io/#/"""

base_url = "https://petstore.swagger.io/v2/"
message = "!Wrong status code!"

"""   USER
Create a new user"""


@pytest.mark.post
def test_new_user():
    data = {
        "id": 11,
        "username": "Katiko",
        "firstName": "Kate",
        "lastName": "Kreis",
        "email": "stringapi@test.com",
        "password": "asdfgH",
        "phone": "+17372527377",
        "userStatus": 0,
    }

    r = requests.post(f"{base_url}user", json=data)
    # print(r.json())
    assert r.status_code == HTTPStatus.OK, message


"""The user login"""


@pytest.mark.get
def test_login():
    login_data = {
        "username": "Katiko",
        "password": "asdfgH",
    }
    r = requests.get(f"{base_url}user/login", json=login_data)
    # print(json.dumps(r.json(), sort_keys=True, indent=4))
    assert r.status_code == HTTPStatus.OK, message


"""The user logout"""


@pytest.mark.get
def test_logout():
    r = requests.get(f"{base_url}user/logout")
    print(json.dumps(r.json(), sort_keys=True, indent=4))
    assert r.status_code == 200, message


"""Update an information about the user"""


@pytest.mark.put
def test_new_info_user():
    new_data = {
        "id": 11,
        "username": "Katya",
        "firstName": "Kate",
        "lastName": "Kreis",
        "email": "stringapi@test.com",
        "password": "asdfgH098",
        "phone": "+17372527311",
        "userStatus": 0,
    }
    r = requests.put(f"{base_url}user/Katiko", json=new_data)
    # json_data = r.json()
    print(json.dumps(r.json(), sort_keys=True, indent=4))
    assert r.status_code == 200, message


"""Get user by user name"""


@pytest.mark.get
def test_user_by_username():
    r = requests.get(f"{base_url}user/Katya")
    # print(json.dumps(r.json(), sort_keys=True, indent=4))
    assert r.status_code == HTTPStatus.OK, message
    json_data = r.json()
    expected_keys = ["email", "firstName", "id", "password", "phone"]
    json_list = []
    for key in json_data.keys():
        json_list.append(key)
    print(json_list)
    assert (x in expected_keys for x in json_list), "!wrong key!"


"""Create a list with users"""


@pytest.mark.post
def test_create_with_list():
    list_data = [
        {
            "id": 12,
            "username": "Mash",
            "firstName": "Maria",
            "lastName": "Lu",
            "email": "luchua@test.com",
            "password": "string",
            "phone": "+11213141516",
            "userStatus": 0,
        },
        {
            "id": 13,
            "username": "Kxen",
            "firstName": "Kseniia",
            "lastName": "KK",
            "email": "qwerty@test.com",
            "password": "12345678",
            "phone": "+11111111111",
            "userStatus": 0,
        },
    ]
    r = requests.post(f"{base_url}user/createWithList", json=list_data)
    assert r.status_code == 200, message
    """And check some user in list"""
    r = requests.get(f"{base_url}user/Kxen", json=list_data)
    # print(r.json())
    assert r.status_code == HTTPStatus.OK, message


"""Delete the user"""


@pytest.mark.delete
def test_delete():
    r = requests.delete(f"{base_url}user/Katya")
    assert r.status_code == HTTPStatus.OK, message

    r = requests.get(f"{base_url}user/Katya")
    assert r.status_code == HTTPStatus.NOT_FOUND, message


"""  PET
A new pet to the store"""


@pytest.mark.post
def test_new_pet():
    pet_data = {
      "id": 10,
      "category": {"id": 1, "name": "Cat"},
      "name": "Pushok",
      "photoUrls": ["https://imageio.forbes.com/specials-images/imageserve/09zFfq433L08b/960x960.jpg"],
      "tags": [{"id": 1, "name": "string"}],
      "status": "available"
    }
    r = requests.post(f"{base_url}pet", json=pet_data)
    assert r.status_code == HTTPStatus.OK, message


