from django.shortcuts import get_object_or_404, redirect, render
from .models import Post
from .forms import PostForm

def posts(request):

    posts = Post.objects.all().order_by('-created_at')
    form=PostForm()
    print(request.POST)
    if request.method=="POST" and 'create' in request.POST:
        form=PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts')
    
    
    if request.method=="POST" and 'update' in request.POST:
        post=get_object_or_404(Post,id=request.POST.get('post_id'))
        form=PostForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts')
    
    if request.method == 'POST' and 'delete' in request.POST:
        post = get_object_or_404(Post, id=request.POST.get('post_id'))
        post.delete()
        return redirect('posts')
    
    
    return render(request, 'blog/index.html', {'posts': posts,'form':form})
