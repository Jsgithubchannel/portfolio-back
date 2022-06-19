from django.db import models

class Project(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    desc = models.TextField()
    qualifications = models.TextField()
    achievements = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(blank=True)

    def __str__(self):
        return self.title

