from django.urls import path
from .views import *

app_name = "main"
urlpatterns = [
    path('', mainpage, name="mainpage"),
    path('second', secondpage, name="secondpage"),
    path('new-post', new_post, name="new-post"),#new_post 함수로 이동
    path('create', create, name="create"),
    path('<int:id>', detail, name="detail"),
    path('edit/<int:id>', edit, name="edit"),
    path('update/<int:id>', update, name="update"),
    path('delete/<int:id>', delete, name="delete"),
    path('tag-lists', tag_list, name="tag_list"),
    path('tag-posts/<int:tag_id>', tag_post, name="tag_post"),
    path('comment-delete/<int:post_id>/<int:comment_id>', comment_delete, name='comment_delete'),
]