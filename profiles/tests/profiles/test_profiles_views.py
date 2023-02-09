import pytest

from django.urls import reverse
from django.test import Client
from pytest_django.asserts import assertTemplateUsed
from django.contrib.auth.models import User
from profiles.models import Profile


@pytest.mark.django_db
def test_index_view():
    client = Client()
    path = reverse("profiles:index")
    response = client.get(path)

    assert response.status_code == 200
    assertTemplateUsed(response, "profiles/index.html")


@pytest.mark.django_db
def test_profile_view():
    client = Client()
    user = User(
        username="4meRomance",
        email="coemperor@famemma.net",
        first_name="John",
        last_name="Rodriguez",
    )
    profile = Profile(user=user, favorite_city="Buenos Aires")
    user.save()
    profile.save()
    path = reverse("profiles:profile", kwargs={"username": profile.user.username})
    response = client.get(path)
    content = response.content.decode()

    assert profile.user.username in content
    assert response.status_code == 200
    assertTemplateUsed(response, "profile.html")
