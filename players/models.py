from django.db import models


class Commander(models.Model):
    name = models.CharField(max_length=100, unique=True)

    fuel = models.IntegerField(default=1000)
    minerals = models.IntegerField(default=500)
    science = models.IntegerField(default=0)

    morale = models.IntegerField(default=100)
    reputation = models.IntegerField(default=50)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
