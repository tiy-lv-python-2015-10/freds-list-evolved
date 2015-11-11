from django.contrib import admin
from fredslist.models import State, City, Category, SubCategory, Post, Images

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('state',)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ( 'city',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('city', 'title',)


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'title',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'sub_category', 'phone_number', 'contact_name', 'posting_title', 'price', 'specific_location', 'postal_code',
        'posting_body', 'post_images')


@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ('post', 'image',)