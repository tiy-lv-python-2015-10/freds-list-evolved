from django.contrib import admin
from peteslist.models import Location, Type, Category, Post, Image, Favorite, \
    Keyword


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'state', 'city')

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'type')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'type', 'category', 'title', 'description', 'phone_number',
                    'contact_name', 'price', 'specific_location', 'condition',
                    'created_at')

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('post', 'image')

@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('post', 'user')

@admin.register(Keyword)
class KeywordAdmin(admin.ModelAdmin):
    list_display = ('keyword', 'user', 'created_at')