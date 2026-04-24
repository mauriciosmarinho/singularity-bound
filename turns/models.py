from django.db import models
from django.utils import timezone


class Turn(models.Model):
    number = models.IntegerField(unique=True)
    processed_at = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.pk:
            last = Turn.objects.order_by("-number").first()
            self.number = 1 if not last else last.number + 1
        super().save(*args, **kwargs)