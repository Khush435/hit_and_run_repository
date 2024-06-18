from django.db import models

class Complaint(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    description = models.TextField()
    date_reported = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
