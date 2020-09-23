## def 함수에서 redirect는 URL로 이동한다.
## def 함수에서 render는 템플릿을 불러온다.
from django.shortcuts import render,redirect,get_object_or_404 #404에러보여준다.
from .models import Post, Comment, Like
from django.contrib.auth.decorators import login_required
from .forms import PostForm

def new(request):
    return render(request, 'post/new.html')

# def create(request):
#     if request.method == "POST":
#         title = request.POST.get('title')
#         content = request.POST.get('content')
#         # image를 입력받을때 input name을 image라고 했으므로 get('image')
#         image = request.FILES.get('image')
#         user = request.user
#         Post.objects.create(title=title, content=content, image=image, user=user)
#         ## create를 하면 title과 content를 Post객체에 담고 posts앱의 main 페이지를 redirect한다.
#         return redirect('posts:main')

@login_required
def create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(user=request.user)
        return redirect('posts:main')
    else:
        form = PostForm()
    return render(request, 'post/post_form.html',{'form':form})

def main(req):
    posts = Post.objects.all().order_by('-created_at')
    return render(req, 'post/main.html', {'posts':posts})

def show(req, id):
    post = Post.objects.get(pk=id)
    post.view_count += 1
    post.save()
    all_comments = post.comments.all()
    return render(req,'post/show.html',{'post':post, 'comments':all_comments})

# def update(req,id):
#     post = get_object_or_404(Post,pk=id)
#     #req 방식이 POST일때만
#     if req.method == "POST":
#         post.title = req.POST.get('title')
#         ##post.title = req.POST['title'] 컬럼명으로 가져오는 방법
#         post.content = req.POST.get('content')
#         ##post.content = req.POST['content']
#         post.image = req.FILES.get('image')
#         # image는 가져올때 POST가 아니라 FILES로 get을 불러온다.
#         post.save()
#         return redirect('posts:show', post.id) #posts앱의 show.html의 url을 다시 연결하겠다.
#     return render(req,'post/update.html',{"post":post}) 
#     #render(request, template이름, 넘겨보낼 딕셔너리형 객체(context))
#     #req 방식이 get방식이라면 update.html을 바로 렌더링한다.

def update(request, id):
    post = get_object_or_404(Post, pk=id)
    form = PostForm(instance=post) # 위에서 불러온 post를 객체로 form에 넣음
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save(user=request.user)
        return redirect('posts:main')
    return render(request, 'post/post_form.html',{'form':form})

#modelForm 상에서도 동일
def delete(req,id):
    post = get_object_or_404(Post,pk=id)
    post.delete()
    return redirect('posts:main')
    #redirect(to(URL) 이동하고자 하는 URL)
    #redirect는 url을 연결한다. 괄호안에는 불러올 viwe의 name

def create_comment(request, id):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=id)
        current_user = request.user
        comment_content = request.POST.get('content')
        Comment.objects.create(content=comment_content, user=current_user, post=post)
    return redirect('posts:show', id)

@login_required
def post_like(request, id):
    post = get_object_or_404(Post, pk=id)

    #좋아요 버튼 확인
    if request.user in post.like_user_set.all():
        post.like_user_set.remove(request.user)
    else:
        post.like_user_set.add(request.user)

    #show, main을 확인하고 redirect한다.
    if request.GET.get('redirect_to')=='show':
        return redirect('posts:show', id)
    else:
        return redirect('posts:main')

@login_required
def like_list(request):

    #방식1 : filter를 활용해서 Like에서 요청자와 같은 object를 추출한다.
    #likes = Like.objects.filter(user==request.user)

    # 요청한 클라이언트에게 연결된 Like에서 object로 likes를 추출한다.
    likes = request.user.like_set.all()
    return render(request, 'post/like_list.html', {'likes':likes})