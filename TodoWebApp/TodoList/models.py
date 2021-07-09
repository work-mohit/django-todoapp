from django.db import models

# Create your models here.
class tododata(models.Model):
    text = models.TextField(blank=False, null=True)

    def __str__(self):
        return self.text[:20]