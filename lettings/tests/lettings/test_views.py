import pytest

from django.urls import reverse
from django.test import Client
from pytest_django.asserts import assertTemplateUsed


@pytest.mark.django_db
def test_index_view():
    client = Client()
    path = reverse("lettings:index")
    response = client.get(path)
    content = response.content.decode()
    expected_content = "<h1>Lettings</h1>"

    assert expected_content in content
    assert response.status_code == 200
    assertTemplateUsed(response, "lettings/index.html")
