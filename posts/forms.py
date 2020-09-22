from django.forms import ModelForm
from .models import Post, Comment

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'image',    
        ]
        # fields = '__all__' 모든 필드를 다 가져온다
        # exclude = ['user'] user필드만 빼고 가져온다.

        labels = {
            'title' : ('제목'),
            'content' : ('내용'),
            'image' : ('이미지'),
        }

        #필드의 사용법을 알려주는 문구
        help_text = {
            'title' : ('제목을 입력해주세요'),
            'content' : ('내용을 입력해주세요'),
        }
    
    #ModelForm 클래스에 내부적으로 있는 메서드
    def save(self, **kwargs):
        post = super().save(commit=False) # 내부에 있는 save() 메서드 호출, commit=false로 데이터가 db에 당장 저장되지는 않음, 
        post.user = kwargs.get('user', None)
        #**kwargs로 넘어온 인자중에 user라는 항목이 있다. post 모델에서 user를 참조하려면 
        post.save()
        return post

# class CommentForm(ModelForm):
#     class Meta:
#         model = Comment
#         fields = [
#             'content',
#         ]
#         labels = {
#             'content': ('댓글'),
#         }
#         help_text = {
#             'content':('댓글을 작성해주세요'),
#         }
    
#     def sav(self, **kwargs):
#         comment = super.save(commit=False)
#         comment.user = kwargs.get('user', None)
#         comment.save()
#         return comment