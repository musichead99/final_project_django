from django import forms
from myPage.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'audio', 'content']
        labels = {
            'title': '제목',
            'audio' : '파일첨부',
            'content': '내용',
        }