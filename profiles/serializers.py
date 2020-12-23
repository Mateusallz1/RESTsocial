from rest_framework import serializers
from profiles.models import Profile, Post, Comment

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class ProfilePostSerializer(serializers.ModelSerializer):
    posts = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = ('name', 'email', 'posts')

class PostSerializer(serializers.ModelSerializer):
    comments = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')

    class Meta:
        model = Post
        fields = ('title', 'body', 'userid', 'comments')
    
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body', 'postid')


class TotalPostCommentSerializer(serializers.Serializer):
    pk = serializers.IntegerField()
    name = serializers.CharField(max_length=128)
    total_posts = serializers.IntegerField()
    total_comments = serializers.IntegerField()

