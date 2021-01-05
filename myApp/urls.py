from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name="index"),
    path('post/', views.post, name="post"),
    path('detail/<int:post_id>/', views.detail, name="detail"),

]
