from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path('gpu/add/', views.AddGPU.as_view(), name='add_gpu'),
    path('gpu/', views.GPUList.as_view(), name='gpu'),
    path('gpu/admin', views.AdminGPUList.as_view(), name='gpu_admin'),
    path('gpu/amd/', views.AMDList.as_view(), name='amd'),
    path('gpu/nvidia/', views.NVIDIAList.as_view(), name='nvidia'),
    path('gpu/<slug:slug>/', views.GPUDetail.as_view(), name='gpu_detail'),
    path('gpu/<slug:slug>/update/', views.UpdateGPU.as_view(), name='update_gpu'),
    path('gpu/<slug:slug>/delete/', views.DeleteGPU.as_view(), name="delete_gpu" ),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('403', views.Error403.as_view(), name='403'),
    path('404', views.Error404.as_view(), name='404'),
    path('500', views.Error500.as_view(), name='500'),
]