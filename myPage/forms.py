from django import forms
from myPage.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'audio', 'content']
        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control'}),
            'audio' : forms.FileInput(attrs={'class' : 'form-control form-control-sm', 'type' : 'file', 'id' : 'formFileSm'}),
            'content' : forms.Textarea(attrs={'class' : 'form-control', 'rows' : 10})
        }
        labels = {
            'title': '제목',
            'audio' : '파일첨부',
            'content': '내용',
        }