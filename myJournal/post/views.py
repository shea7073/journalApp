from django.shortcuts import render, redirect
from .forms import PostForm
from django.contrib import messages


def addPost(request):
    form = PostForm()
    
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.owner = request.user
            form.save()
            messages.success(request, 'Post successfully added')
            return redirect('home')

    context = {'form': form}
    return render(request, 'post.html', context)
