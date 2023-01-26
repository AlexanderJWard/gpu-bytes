from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('gpu/add/', views.AddGPU.as_view(), name='add_gpu'),
    path('add/', views.AddPost.as_view(), name='add_post'),
    path('gpu/', views.GPUList.as_view(), name='gpu'),
    path('gpu/admin/', views.AdminGPUList.as_view(), name='gpu_admin'),
    path('post/admin/', views.AdminPostList.as_view(), name='post_admin'),
    path('gpu/amd/', views.AMDList.as_view(), name='amd'),
    path('gpu/nvidia/', views.NVIDIAList.as_view(), name='nvidia'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('gpu/<slug:slug>/', views.GPUDetail.as_view(), name='gpu_detail'),
    path('gpu/<slug:slug>/update/', views.UpdateGPU.as_view(), name='update_gpu'),  # noqa
    path('<slug:slug>/update/', views.UpdatePost.as_view(), name='update_post'),  # noqa
    path('gpu/<slug:slug>/delete/', views.DeleteGPU.as_view(), name='delete_gpu'),  # noqa
    path('<slug:slug>/delete/', views.DeletePost.as_view(), name='delete_post'),  # noqa
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('403', views.Error403.as_view(), name='403'),
    path('404', views.Error404.as_view(), name='404'),
    path('500', views.Error500.as_view(), name='500'),
]
