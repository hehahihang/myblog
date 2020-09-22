from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=50, null=False)
    content = models.TextField()
    view_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    image = models.ImageField(upload_to='images/',null=True) #upload_to 는 저장경로
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    like_user_set = models.ManyToManyField(User, blank=True, related_name="like_user_set", through='Like')
    #through == Like라는 클래스를 통해서 lise_user_set을 연결해주기위함


# model을 수정하고나면 make migrations해서 변경된부분을 확인하고
# migrate로 수정한다. 
class Comment(models.Model):
    objects = models.Manager()
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    # related_name : post 에서도 comments를 볼 수 있도록 연결
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


class Like(models.Model):
    objects = models.Manager()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #함께 가져와서 고유해야하는 필드 이름 세트
    class Meta:
        unique_together = (('user','post'))
