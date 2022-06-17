from django.http import FileResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from django.core.files.storage import FileSystemStorage
from .models import Post
from .forms import PostForm

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

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            print(request.FILES['audio'])
            post.create_date = timezone.now()
            post.save()
            return redirect('myPage:index')
    else:
        form = PostForm()
    context = {'form': form}
    return render(request, 'myPage/post_form.html', context)

def audio_download(request, post_id):
    post = Post.objects.get(id=post_id)
    path = post.audio.path
    type = "application/octet-stream"
    fs = FileSystemStorage(path)
    response = FileResponse(fs.open(path, 'rb'), content_type = type)
    response['Content-Disposition'] = f'attachment; filename={post.audio.name}'
    return response
