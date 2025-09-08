from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter post title'}),
            'body': forms.Textarea(attrs={'placeholder': 'Enter post content'}),
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 5:
            raise forms.ValidationError('Title must be at least 5 characters long.')
        return title