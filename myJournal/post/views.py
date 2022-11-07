from django.shortcuts import render
from .forms import PostForm


def addPost(request):
    form = PostForm()
    
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'post.html', context)
