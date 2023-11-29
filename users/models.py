from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=500, blank=True, null=True)
    photo = models.ImageField(upload_to='users/', blank=True, null=True)


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    def edit(self, new_text):
        self.text = new_text
        self.save()

    def delete(self):
        self.delete()
