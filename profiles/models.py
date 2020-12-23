from django.db import models
# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()    
    
    def total_posts(self):
        total = Post.objects.filter(userid=self).count()
        return total

    def total_comments(self):
        total = Comment.objects.filter(postid__userid=self).count()
        return total

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
        
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=500)
    userid = models.ForeignKey(Profile, related_name='posts', on_delete=models.CASCADE)

    class Meta:
        ordering = ('title',)
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()
    body = models.CharField(max_length=500)
    postid = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)