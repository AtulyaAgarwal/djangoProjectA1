from django.shortcuts import render
posts = [
    {
        'author': 'Guy',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'July 19, 2024'
    },
    {
        'author': 'Girl',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'June 18, 2024'
    }
]
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html',context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
