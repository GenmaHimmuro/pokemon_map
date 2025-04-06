from django.db import models  # noqa F401

class Pokemon(models.Model):
    title = models.TextField()

    def __str__(self):
        if self.title:
            return self.title
