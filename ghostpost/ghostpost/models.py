from django.db import models
from django.utils import timezone

class GhostPost(models.Model):
    ghostTitle = models.CharField(max_length=50)
    body = models.TextField(max_length=280)
    is_boast = models.BooleanField()
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    total_votes = models.IntegerField(default=0)
    post_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.ghostTitle}"