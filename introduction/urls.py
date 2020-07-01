from django.urls import path
from . import views
#from . 은 현재 디렉토리

app_name = 'introduction'
urlpatterns = [
    path('', views.profile, name="profile"),
    #url이 비어있을때 views.py의 def profile을 불러오기 위해서 view도 imports 해준다.
]