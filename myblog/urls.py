"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include 
from . import views 

#앱의 url을 view와 연결하기 위해서는 각 html이 있는 경로를 import 해야한다.
#introduction으로 시작하는 url은 include를 사용해서 introduction.urls라고 하는 파일에서 관리한다.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('introduction/', include('introduction.urls')),
    path('', views.main, name="main"),
]
