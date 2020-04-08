from django.contrib.auth.models import models
# from jsonfield import JSONField

class Cow_Model(models.Model):
    def __str__(self):
        return self.cow_says

    cow_says = models.CharField(max_length=500)
    # cow_said = JSONField()