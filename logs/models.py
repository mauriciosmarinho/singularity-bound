from django.db import models


class LogEntry(models.Model):
    turn = models.IntegerField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[T{self.turn}] {self.message[:50]}"
