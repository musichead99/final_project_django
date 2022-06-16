from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from .models import Post

def index(request) :
    post_list = Post.objects.order_by('-create_date')
    context = {'post_list' : post_list}
    return render(request, 'myPage/post_list.html', context)

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {'post' : post}
    return render(request, 'myPage/post_detail.html', context)

def comment_create(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.comment_set.create(content=request.POST.get('content'), create_date=timezone.now())
    return redirect('myPage:detail', post_id=post.id)