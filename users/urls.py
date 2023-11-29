from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path("signup/", views.SignUp.as_view(), name="signup"),
    path("users/", views.users, name="users"),
    path('edit_profile/', views.edit_profile, name='profile'),
    path("blogs/", views.blogs, name="blogs"),
    path("create_post/", views.create_post, name="create_post"),
    path("edit_post/<int:post_id>/", views.edit_post, name="edit_post"),
    path("post_detail/<int:post_id>/", views.edit_post, name="post_detail"),
]