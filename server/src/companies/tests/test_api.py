import json
import pytest
from django.urls import reverse

from companies.models import Company
from users.models import User


pytestmark = [pytest.mark.django_db]
companies_url = reverse("companies:company-list")

@pytest.fixture
def client(client, user):
    client.force_login(user)
    client.login(email='test@mail.ru', is_admin=True, is_staff=True)
    return client

@pytest.fixture
def user(mixer):
    user = mixer.blend(User, email="test@gmail.com", is_admin=True, is_staff=True)
    user.set_password('test')
    user.save()
    return user

@pytest.fixture
def company(user):
    company = Company.objects.create(name="Test Company", user=user)
    return company


def test_get_company_api(client, company):
    response = client.get(companies_url)
    response_content = json.loads(response.content)[0]
    assert response.status_code == 200
    assert response_content.get("name") == company.name

def test_get_companies_api(client):
    response = client.get(companies_url)
    assert response.status_code == 200
    
def test_delete_company_api(client, company):
    id = company.id
    response = client.delete(f'/company/{id}/delete/')
    assert response.status_code == 200

def test_create_company_api(client, user):
    response = client.post('/company/create/', {'name': 'Test Name', 'user': user})
    response_content = json.loads(response.content)
    assert response.status_code == 201
    assert response_content.get("name") == 'Test Name'

def test_edit_company_api(client, company):
    id = company.id
    response = client.put(f'/company/companies-api/{id}/', {'name': 'New test name'}, content_type='application/json')
    response_content = json.loads(response.content)
    assert response.status_code == 200
    assert response_content.get("name") == 'New test name'