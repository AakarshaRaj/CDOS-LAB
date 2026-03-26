from mixer.backend.django import mixer
import pytest
@pytest.mark.django_db
class TestModels:
    def test_reading_break(self):
        read = mixer.blend('movies.Movie', duration=120)
        assert read.is_post_production_completed == True
