from django import forms
from django.forms import Textarea
from fredslist.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'user', 'sub_category', 'phone_number', 'contact_name', 'posting_title', 'price', 'specific_location',
            'postal_code', 'location',
            'posting_body',)



# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = (
#             'user', 'sub_category', 'phone_number', 'contact_name', 'posting_title', 'price', 'specific_location',
#             'postal_code', 'location',
#             'posting_body',)
#         widgets = {
#             'message': Textarea(attrs={'rows': 2})
#         }
