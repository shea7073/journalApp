from django.shortcuts import render
from post.models import Post
from django.core.paginator import Paginator

# Create your views here.
def show_posts(request):
    user_posts = Post.objects.filter(owner=request.user)

    p = Paginator(Post.objects.filter(owner=request.user).order_by('post_date'), 1)
    page = request.GET.get('page')
    if not page:
        page = p.num_pages
    posts = p.get_page(page)


    return render(request, 'my_posts.html/' , {'user_posts': user_posts, 'posts': posts})