from django.db import models


class Faction(models.Model):
    name = models.CharField(max_length=100, unique=True)
    relation = models.IntegerField(default=50)

    def mood(self):
        if self.relation >= 70:
            return "Amistosa"
        elif self.relation >= 40:
            return "Neutra"
        return "Hostil"

    def __str__(self):
        return self.name
        
class ResearchProject(models.Model):
    name = models.CharField(max_length=100, unique=True)
    turns_remaining = models.IntegerField(default=3)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name
        
class Sector(models.Model):
    name = models.CharField(max_length=50, unique=True)
    discovered = models.BooleanField(default=True)
    description = models.TextField()

    colonized = models.BooleanField(default=False)
    owner = models.CharField(max_length=100, blank=True, default="")

    def __str__(self):
        return self.name
        
class Fleet(models.Model):
    name = models.CharField(max_length=100, unique=True)
    power = models.IntegerField(default=100)
    status = models.CharField(max_length=50, default="Operacional")

    def __str__(self):
        return self.name

class Leader(models.Model):
    name = models.CharField(max_length=100, unique=True)
    role = models.CharField(max_length=100)
    bonus = models.CharField(max_length=200)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name