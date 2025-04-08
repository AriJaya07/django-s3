from django.db import models

class UploadedImage(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
