import pytest
from django.urls import reverse

pytest.mark.django_db


def test_get_as_anonymous(client):
    # When:
    #   A non-logged in user tries to access the view
    r = client.get(reverse("manual-cache-invalidation"))
    # Then:
    #   They should be redirected to the login page
    assert r.status_code == 302
    assert r.url.startswith(reverse("wagtailadmin_login"))


def test_get_as_admin(admin_client):
    # When:
    #   An admin user tries to access the view
    r = admin_client.get(reverse("manual-cache-invalidation"))
    # Then:
    #   They should be able to access the view
    assert r.status_code == 200
    assert "invalidatecache/admin/form.html" in [t.name for t in r.templates]


def test_post_as_anoymous(client):
    # When:
    #   A non-logged in user tries to access the view
    r = client.post(reverse("manual-cache-invalidation"))
    # Then:
    #   They should be redirected to the login page
    assert r.status_code == 302
    assert r.url.startswith(reverse("wagtailadmin_login"))


def test_post_as_admin_success(admin_client, mock_myserver):
    # When:
    #   An admin user tries to invalidate the cache of a valid tag
    r = admin_client.post(reverse("manual-cache-invalidation"), {"tag": "pages"})
    # Then: Redirect to success url
    assert r.status_code == 302
    # (follow)
    r = admin_client.get(r.url)
    assert "Successfully invalidated cache for tag pages" in r.content.decode()


def test_post_as_admin_failed_request(admin_client, mock_myserver):
    # Given:
    mock_myserver.post("https://myserver.com/invalidate-cache/", status_code=400)
    # When:
    #   An admin user tries to invalidate the cache of an invalid tag
    r = admin_client.post(reverse("manual-cache-invalidation"), {"tag": "invalid"})
    # Then: Redirect to success url (but with error message)
    assert r.status_code == 302
    # (follow)
    r = admin_client.get(r.url)
    assert "Error invalidating cache for tag invalid" in r.content.decode()


def test_missing_tag(admin_client, mock_myserver):
    # When:
    #   An admin user tries to invalidate the cache without specifying a tag
    r = admin_client.post(reverse("manual-cache-invalidation"))
    # Then: They should get an error message
    assert r.status_code == 200
    assert "form" in r.context
    assert r.context["form"].errors == {"tag": ["Dette feltet er påkrevet."]}


def test_blank_tag(admin_client, mock_myserver):
    # When:
    #   An admin user tries to invalidate the cache without specifying a tag
    r = admin_client.post(reverse("manual-cache-invalidation"), {"tag": ""})
    # Then: They should get an error message
    assert r.status_code == 200
    assert "form" in r.context
    assert r.context["form"].errors == {"tag": ["Dette feltet er påkrevet."]}
