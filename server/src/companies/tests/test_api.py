import json
import pytest
from django.urls import reverse
from companies.models import Company


pytestmark = [pytest.mark.django_db]
companies_url = reverse("companies:company-list")


def test_get_company_api(client, django_user_model):
    user = django_user_model.objects.create_user(email='test@mail.ru', password='test', is_admin=True, is_staff=True)
    client.force_login(user)
    client.login(email='test@mail.ru', password='test')
    test_company = Company.objects.create(name="Test Company")
    response = client.get(companies_url)
    response_content = json.loads(response.content)[0]
    assert response.status_code == 200
    assert response_content.get("name") == test_company.name

    test_company.delete()

def test_get_companies_api(client, django_user_model):
    user = django_user_model.objects.create_user(email='test@mail.ru', password='test', is_admin=True, is_staff=True)
    client.force_login(user)
    client.login(email='test@mail.ru', password='test')

