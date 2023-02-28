import pytest

from django.urls import reverse
from django.test import Client
from pytest_django.asserts import assertTemplateUsed
from lettings.models import Letting, Address


@pytest.mark.django_db
def test_index_view():
    client = Client()
    path = reverse("lettings:index")
    response = client.get(path)

    assert response.status_code == 200
    assertTemplateUsed(response, "lettings/index.html")


@pytest.mark.django_db
def test_letting_view():
    client = Client()
    address = Address(
        number=7217,
        street="Bedford Street",
        city="Brunswick",
        state="GA",
        zip_code=31525,
        country_iso_code="USA",
    )
    letting = Letting(title="Joshua Tree Green Haus /w Hot Tub", address=address)
    address.save()
    letting.save()
    path = reverse("lettings:letting", kwargs={"letting_id": 1})
    response = client.get(path)
    content = response.content.decode()

    assert letting.title in content
    assert response.status_code == 200
    assertTemplateUsed(response, "letting.html")
