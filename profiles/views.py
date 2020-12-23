from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.reverse import reverse

from profiles.models import Profile, Post, Comment
from profiles.serializers import ProfileSerializer, ProfilePostSerializer, PostSerializer, CommentSerializer, TotalPostCommentSerializer
# Create your views here.

class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    name = 'profile-list'


class ProfileDetail(generics.RetrieveDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    name = 'profile-detail'


class ProfilePost(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfilePostSerializer
    name = 'profile-posts'


class PostComment(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name = 'post-comments'


class PostCommentDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name = 'post-comments'


class CommentView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    name = 'comment'

    def get_queryset(self):
        queryset = Comment.objects.filter(postid=self.kwargs.get('postid'))
        return queryset


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    name = 'comment-detail'

    
class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'profile': reverse(ProfileList.name, request=request),
            'profile-posts': reverse(ProfilePost.name, request=request),
            'post-comments': reverse(PostComment.name, request=request),
        })


class TotalPostComment(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        profile = Profile.objects.get(id=kwargs['pk'])
        total_posts = profile.total_posts()
        total_comments = profile.total_comments()
        data = {'pk': profile.id, 'name': profile.name, 'total_posts': total_posts, 'total_comments': total_comments}
        serializer = TotalPostCommentSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)
    name = 'total-posts-comments'