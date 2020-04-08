from django.db import models


class Post(models.Model):
    # We will need an ID, but can use pk for this
    is_boast = models.BooleanField()
    contents = models.CharField(max_length=280)
    up_votes = models.IntegerField()
    down_votes = models.IntegerField()
    submission_time: models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.contents
