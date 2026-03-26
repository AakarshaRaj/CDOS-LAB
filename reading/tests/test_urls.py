from django.urls import reverse, resolve
import pytest
from django.contrib.auth.models import User
from reading.models import ReadingSession

@pytest.mark.django_db
def test_create_session():
    user = User.objects.create_user(username='test', password='123')

    session = ReadingSession.objects.create(
        user=user,
        book_title="Test Book",
        duration=30,
        break_time=10
    )

    assert session.book_title == "Test Book"