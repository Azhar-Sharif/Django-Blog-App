"""
URL configuration for blog_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path,include
from django.contrib.auth.views import LoginView, LogoutView
from blog.views import home_view, post_create, post_update, post_delete, signup,comment_create

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home_view, name='home'),
    path("post/new/",post_create,name="post_create"),
    path("post/<int:post_id>/edit/",post_update, name ="post_update"),
    path("post/<int:post_id>/delete/",post_delete,name="post_delete"),
    path('post/<int:post_id>/comment/', comment_create, name='comment_create'),
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('signup/', signup, name='signup'), 
]
