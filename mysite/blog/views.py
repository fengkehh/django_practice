from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post


# Create your views here.
def post_list(request):
    # Use the Post published manager to display only published posts.
    all_posts = Post.published.all()
    paginator = Paginator(all_posts, 3) # 3 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # if page is not an integer deliver the first page
        # posts = posts to be displayed in the delivered page
        posts = paginator.page(1)
    except EmptyPage:
        # if page is out of range deliver last page of result
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/post/list.html',
                  {'page': page, 'posts': posts})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug = post,
                             status = 'published',
                             publish__year = year,
                             publish__month = month,
                             publish__day = day)

    return render(request, 'blog/post/detail.html', {'post': post})