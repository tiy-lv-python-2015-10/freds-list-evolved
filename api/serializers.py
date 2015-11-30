from django.contrib.auth.models import User
from rest_framework import serializers
from peteslist.models import Post


class PostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = Post
        fields = ('id', 'user', 'type', 'category', 'title', 'description',
                  'location', 'phone_number', 'contact_name', 'price',
                  'specific_location', 'condition', 'by_phone', 'by_text',
                  'created_at', 'favorite_count')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'post_set')
