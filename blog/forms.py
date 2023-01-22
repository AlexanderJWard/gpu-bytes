from .models import Comment, GPU
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body', 'brand',)

class GPUForm(forms.ModelForm):

    class Meta:
        model = GPU
        fields = ('name', 'gpu_brand', 'image', 'content', 'specs', 'date_released', 'status', 'memory_size', 'memory_type', 'base_clock', 'boost_clock')