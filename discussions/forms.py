from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    body = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Say Hi!'}),
        max_length=255,
        label='Comment Here')

    class Meta:
        model = Comment
        fields = ('body',)
