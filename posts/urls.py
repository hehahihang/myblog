from django.urls import path
from .views import *

app_name = "posts"

urlpatterns = [
    #path(path/, 일치하는 url패턴을 찾으면 불러올 view의 함수 def를 호출한다, 이 경로의 이름)
    path('new/', new, name="new"),
    path('create/', create, name="create"),
    path('', main, name="main"),
    path('show/<int:id>', show, name="show"),
    path('update/<int:id>', update, name="update"),
    path('deltete/<int:id>', delete, name="delete"),
    path('create_comment/<int:id>', create_comment, name="create_comment"),
    path('post_like/<int:id>', post_like, name="post_like"),
    path('like_list/', like_list, name="like_list"),
]