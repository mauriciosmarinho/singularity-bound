from django.db import models


class Turn(models.Model):
    number = models.IntegerField(default=1)
    processed_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Turn {self.number}"
