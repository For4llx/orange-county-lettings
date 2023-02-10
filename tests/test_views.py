import pytest

from django.urls import reverse
from django.test import Client
from pytest_django.asserts import assertTemplateUsed


@pytest.mark.django_db
def test_index_view():
    client = Client()
    path = reverse("index")
    response = client.get(path)

    assert response.status_code == 200
    assertTemplateUsed(response, "index.html")
