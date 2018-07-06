from django.shortcuts import render, get_object_or_404

from blog.models import Post


def allblogs(request):
    blog_posts = Post.objects
    return render(request, 'blog/allblogs.html', {'posts': blog_posts})


def detail(request, blog_id):
    details = get_object_or_404(Post, pk=blog_id)
    return render(request, 'blog/detail.html', {'detailed_post': details})
