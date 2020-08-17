from django.urls import path
from . import views

urlpatterns = [
    path('', views.redirect_home, name='redirect'),
    path('homepage/', views.home, name='homepage'),
    path('profile/<slug:username>', views.user_profile, name='profile'),
    path('post-delete/<int:pk>', views.delete, name='post_delete'),
    path('posts/', views.post_list, name='post_titles'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('create-account/', views.register, name='create_account'),
]
