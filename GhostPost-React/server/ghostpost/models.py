from django.db import models


class Post(models.Model):
    is_boast = models.BooleanField()
    contents = models.CharField(max_length=280)
    up_votes = models.IntegerField(default=0)
    down_votes = models.IntegerField(default=0)
    submission_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.contents


