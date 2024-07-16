# will take the model and convert to JSON
from rest_framework import serializers
from .models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        # fields = '__all__'
        fields = ['id', 'title', 'content', 'date_posted']
        