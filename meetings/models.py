from django.db import models

class Meeting(models.Model):
    title = models.CharField(max_length=200)
    audio = models.FileField(upload_to='meetings/')
    transcript = models.TextField(blank=True)
    summary = models.TextField(blank=True)
    action_items = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title