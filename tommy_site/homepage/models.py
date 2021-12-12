from django.db import models

# Create your models here.
class Intro(models.Model):
    intro = models.TextField()
    def __str__(self):
        return f"{self.intro}"
