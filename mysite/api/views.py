from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
# Create your views here.
from .models import BlogPost
from .serializers import BlogPostSerializer
from rest_framework.views import APIView

class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all() # get all the blog posts
    serializer_class = BlogPostSerializer # convert to JSON

    def delete(self, request, *args, **kwargs):
        BlogPost.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = 'pk'


class BlogPostList(APIView):
    def get(self, request):
        title = request.query_params.get('title', None)

        if title:
            blogposts = BlogPost.objects.filter(title__icontains=title)
        else:
            blogposts = BlogPost.objects.all() # get all the blog posts
        serializer = BlogPostSerializer(blogposts, many=True) # convert to JSON # many=True means we are converting multiple objects
        return Response(serializer.data) # return JSON

    def post(self, request):
        serializer = BlogPostSerializer(data=request.data) # convert JSON to model
        if serializer.is_valid():   # check if the data is valid
            serializer.save() # save the data
            return Response(serializer.data, status=status.HTTP_201_CREATED)   # return the data
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # return the error


