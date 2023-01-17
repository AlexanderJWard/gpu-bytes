from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path('gpu/add/', views.AddGPU, name='add_gpu'),
    path('gpu/', views.GPUList.as_view(), name='gpu'),
    path('gpu/amd/', views.AMDList.as_view(), name='amd'),
    path('gpu/nvidia/', views.NVIDIAList.as_view(), name='nvidia'),
    path('gpu/<slug:slug>/', views.GPUDetail.as_view(), name='gpu_detail'),
    path('gpu/<slug:slug>/edit/', views.EditGPU, name='edit_gpu'),
    path('gpu/<slug:slug>/delete/', views.DeleteGPU, name="delete_gpu" ),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]