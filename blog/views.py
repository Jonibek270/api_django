from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.utils import timezone
from blog.models import Post
from .serializers import PostSerializer

class PostList(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(
            {
                "status": status.HTTP_200_OK,
                "data":{
                    "posts":serializer.data,
                    "count":len(serializer.data)
            },
                "message": "Serverdan postlar keldi!",
                "timestamp": timezone.localtime(timezone.now())
            }
        )