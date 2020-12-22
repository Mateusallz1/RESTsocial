from django.urls import path
from profiles import views

urlpatterns = [
    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),
    path('profiles/', views.ProfileList.as_view(), name=views.ProfileList.name),
    path('profiles/<int:pk>/', views.ProfileDetail.as_view(), name=views.ProfileDetail.name),
    path('profile-posts/', views.ProfilePost.as_view(), name=views.ProfilePost.name),
    path('post-comments/', views.PostComment.as_view(), name=views.PostComment.name),
    path('post-comments/<int:pk>/', views.PostCommentDetail.as_view(), name=views.PostCommentDetail.name),
    path('post/<int:postid>/comments/', views.CommentView.as_view(), name=views.CommentView.name),
    path('post/<int:postid>/comments/<int:pk>/', views.CommentDetailView.as_view(), name=views.CommentDetailView.name)
]
 