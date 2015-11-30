from django.contrib.auth.models import User
from django.db import models


class Location(models.Model):
    state = models.CharField(max_length=25)
    city = models.CharField(max_length=40)

    def __str__(self):
        return "{}, {}".format(self.city, self.state)


class Type(models.Model):
    title = models.CharField(max_length=25)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=35)
    type = models.ForeignKey(Type)

    def __str__(self):
        return self.title


class Post(models.Model):

    CONDITION_CHOICES = (
        ('new', 'New'),
        ('like new', 'Like New'),
        ('excellent', 'Excellent'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('salvage', 'Salvage'),
        ('other', 'Other')
        )

    user = models.ForeignKey(User)
    type = models.ForeignKey(Type, null=True)
    category = models.ForeignKey(Category, null=True)
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=5000)
    location = models.ForeignKey(Location, null=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    contact_name = models.CharField(max_length=35, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,
                                null=True, blank=True)
    specific_location = models.CharField(max_length=75, null=True, blank=True)
    condition = models.CharField(choices=CONDITION_CHOICES, null=True,
                                 blank=True, max_length=20)
    by_phone = models.BooleanField(default=False)
    by_text = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    @property
    def favorite_count(self):
        return self.favorite_set.all().count()

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField(upload_to='peteslist_images')
    post = models.ForeignKey(Post, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)


class Favorite(models.Model):
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return "Favorite: {}".format(self.post.title)


class Keyword(models.Model):
    keyword = models.CharField(max_length=50)
    user = models.ForeignKey(User, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.keyword
