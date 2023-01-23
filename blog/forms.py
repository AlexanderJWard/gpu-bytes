from .models import Comment, GPU, Post
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body', 'brand',)

class GPUForm(forms.ModelForm):

    class Meta:
        model = GPU
        fields = ('name', 'gpu_brand', 'image', 'date_released', 'content', 'sourced_from', 'specs', 'memory_size', 'memory_type', 'base_clock', 'boost_clock', 'status')


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'featured_image', 'content', 'excerpt', 'status')