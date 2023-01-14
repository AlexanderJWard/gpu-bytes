from .models import Comment, GPU
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body', 'brand',)

class AddGPUForm(forms.ModelForm):

    class Meta:
        model = GPU
        fields = ('name', 'brand', 'image', 'content', 'specs', 'date_released', 'status',)