from django.shortcuts import render, HttpResponse
from .models import Post

# Create your views here.
def blog_list(request):
    posts = Post.objects.all()
    post_list = ''
    html = '''<h1>Blog</h1>'''
    for post in posts:
        post_list += f'<li><a href="{post.slug}">{post.title}</a></li>'
    return HttpResponse(f"<ul>{post_list}</ul>")
