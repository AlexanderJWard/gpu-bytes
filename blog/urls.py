from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path('add_gpu/', views.AddGPU, name='add_gpu'),
    path('amd/', views.AMDList.as_view(), name='amd'),
    path("nvidia/", views.NVIDIAList.as_view(), name="nvidia"),
    path('gpu/<slug:slug>/', views.GPUDetail.as_view(), name='gpu_detail'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]