from django import forms
from django.contrib.auth.models import User
from .models import Post,Comment

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
    

class UserCreationForm(forms.ModelForm):
       password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
       password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

       class Meta:
           model = User
           fields = ['username', 'email']

       def clean_password2(self):
           password1 = self.cleaned_data.get('password1')
           password2 = self.cleaned_data.get('password2')
           if password1 and password2 and password1 != password2:
               raise forms.ValidationError('Passwords do not match.')
           return password2

       def save(self, commit=True):
           user = super().save(commit=False)
           user.set_password(self.cleaned_data['password1'])
           if commit:
               user.save()
           return user
       
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Add a comment...'}),
        }