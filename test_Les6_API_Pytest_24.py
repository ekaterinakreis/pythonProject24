import pytest
import requests

# def sum_it(x, y):
#     return x + y

# def test_equal():
#     assert sum_it(5, 3) == 8
#
# def test_negative():
#     assert sum_it(4, 8) == 11

base_url = 'https://restful-booker.herokuapp.com/booking'
auth_url = "https://restful-booker.herokuapp.com/auth"

@pytest.fixture(scope = 'module')
def auth_token():
    authdata = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(auth_url, json = authdata)
    token = response.json()["token"]
    yield token

@pytest.fixture(scope= 'session')
def booking_id():
    payload = {
        "firstname": "James",
        "lastname": "Brown",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-02-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(base_url, json=payload)
    yield response.json()['bookingid']

@pytest.mark.smoke
def test_get_code():
    result = requests.get(base_url)
    print(result.json())
    assert result.status_code == 200

# booking id changes often!

@pytest.mark.skip
def test_get_booking_by_id():
    response = requests.get(f'{base_url}/1')
    response_data = response.json()
    expected_keys = {
        "firstname",
        "lastname",
        "totalprice",
        "depositpaid",
        "bookingdates"
    }
    # print(response_data)
    assert response.status_code == 200
    assert len(expected_keys) == len(response_data.keys())
    for key in expected_keys:
        assert key in response_data.keys()

# def test_create_booking():
#
#     payload = {
#     "firstname" : "James",
#     "lastname" : "Brown",
#     "totalprice" : 150,
#     "depositpaid" : True,
#     "bookingdates" : {
#         "checkin" : "2018-01-01",
#         "checkout" : "2019-02-01"
#     },
#     "additionalneeds" : "Breakfast"
# }
#     response = requests.post(base_url, json=payload)
#     print(response.json()['bookingid'])
#     assert response.status_code == 200

@pytest.mark.regression
@pytest.mark.xfail(reason ='wrong status code')
def test_check_crated_booking(booking_id):
    result = requests.get(f'{base_url}/{booking_id}')
    print(result.json())
    assert result.status_code == 200
    assert result.json()['firstname'] == "James"


def test_update_booking(auth_token, booking_id):
    payload = {
    "firstname" : "James",
    "lastname" : "Brown",
    "totalprice" : 150,
    "depositpaid" : False,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-02-01"
    },
    "additionalneeds" : "Lunch"
}
    token = {"Cookie": f'token = {auth_token}'}
    response = requests.put(f'{base_url}/{booking_id}', json = payload, headers = token)
    assert response.status_code == 200
    response2 = requests.get(f'{base_url}/{booking_id}')
    print(response2.json())
    assert response2.json()["additionalneeds"] == "Lunch"

# def test_options():
#     response = requests.options(f'{base_url}/1')
#     assert response.status_code == 200
#     print(response.json())
#
# def test_head():
#     response = requests.head(f'{base_url}/1')
#     assert response.status_code == 200
#     print(response.headers)

def test_delete_booking(booking_id, auth_token):
    token = {"Cookie": f'token = {auth_token}'}
    response = requests.delete(f'{base_url}/{booking_id}', headers=token)
    assert response.status_code == 201
    responsse_get = requests.get(f'{base_url}/{booking_id}')
    assert responsse_get.status_code == 404