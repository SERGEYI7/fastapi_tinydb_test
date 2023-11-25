import httpx
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_form_not_valid_email():
    response: httpx.Response = client.post("/get_form",params={"email": "adsads.asd",
                                                   "phone": ""})
    assert response.status_code == 200
    assert response.json() == {'email': 'value is not a valid email address: The email address is not valid. It must have exactly one @-sign.'}


def test_get_form_not_valid_phone():
    response: httpx.Response = client.post("/get_form",params={"email": "ads@ads.asd",
                                                   "phone": "24r24r"})
    assert response.status_code == 200
    assert response.json() == {'phone': 'Number phone invalid'}


def test_get_form_not_valid_email_and_not_valid_phone():
    response: httpx.Response = client.post("/get_form",params={"email": "adsads.asd",
                                                   "phone": "24et42t"})
    assert response.status_code == 200
    assert response.json() == {'email': 'value is not a valid email address: The email address is not valid. It must have exactly one @-sign.', 'phone': 'Number phone invalid'}


def test_get_form_not_email():
    response: httpx.Response = client.post("/get_form",params={
                                                   "phone": ""})
    assert response.status_code == 200
    assert response.json() == {'email': 'missing argument email'}


def test_get_form_not_phone():
    response: httpx.Response = client.post("/get_form",params={"email": "adsads.asd",
                                                   })
    assert response.status_code == 200
    assert response.json() == {'phone': 'missing argument phone'}


def test_get_form_not_email_and_not_phone():
    response: httpx.Response = client.post("/get_form",params={})
    assert response.status_code == 200
    assert response.json() == {'email': 'missing argument email', 'phone': 'missing argument phone'}

def test_get_form_valid():
    response: httpx.Response = client.post("/get_form",params={"email": "ivanov@example.com",
                                                                   "phone": "+9876543210"})
    assert response.status_code == 200
    assert response.json() == ['Иванов Иван']

test_get_form_not_valid_email()
test_get_form_not_valid_phone()
test_get_form_not_valid_email_and_not_valid_phone()
test_get_form_not_email()
test_get_form_not_phone()
test_get_form_not_email_and_not_phone()
test_get_form_valid()
