import json
import pytest
from unittest import TestCase
from django.http import response
from django.test import Client
from django.urls import reverse


@pytest.mark.django_db
class TestGetCompnaies(TestCase):
    
    def setUp(self) -> None:
        self.client = Client()
        self.companies_url = reverse("companies-list")

    def test_get_companies(self):
        response = self.client.get(self.companies_url)
        self.assertEqual(response.status_code, 200)