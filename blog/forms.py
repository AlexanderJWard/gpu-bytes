from .models import Comment, GPU, Post
from django import forms

"""
Form containg relevant fields from the Comment model
"""
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('body', 'brand',)

"""
Form containg relevant fields from the GPU model
"""
class GPUForm(forms.ModelForm):

    class Meta:
        model = GPU
        fields = ('name', 'gpu_brand', 'image', 'date_released', 'content', 'sourced_from', 'specs', 'memory_size', 'memory_type', 'base_clock', 'boost_clock', 'status')

"""
Form containg relevant fields from the Post model
"""
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'featured_image', 'content', 'sourced_from', 'excerpt', 'status')