from django.db import models
from fredslist.models import Post


class UserProfile(models.Model):
    favorites = models.ManyToManyField(Post, related_name='favorited_by')




#somehow use sessions and cookies to remember location
