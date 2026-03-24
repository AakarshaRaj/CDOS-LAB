from django.contrib.auth.models import User
from django.db import models

class ReadingSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book_title = models.CharField(max_length=200)
    duration = models.IntegerField()
    break_time = models.IntegerField()
    start_time = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.book_title)


class Note(models.Model):
    session = models.ForeignKey(ReadingSession, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.content)[:20]