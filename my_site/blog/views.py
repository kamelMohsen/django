from django.http.response import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpRequest
from django.urls import reverse

blogs = {
"What is Programming": 
'''
Computer programs (or software) are what make computers work. Without software, modern computers are just complicated machines for turning electricity into heat. It’s software on your computer that runs your operating system, browser, email, games, movie player – just about everything.
Programming is a creative task: there is no right or wrong way to solve a problem, in the same way that there is no right or wrong way to paint a picture. There are choices to be made, and one way may seem better than another, but that doesn’t mean the other is wrong! With the right skills and experience, a programmer can craft software to solve an unlimited number of problems – from telling you when your next train will arrive to playing your favourite music. The possibilities are constrained only by your imagination. That’s why I love programming.
'''
}
# Create your views here.
def index(request):
    blog_titles = list(blogs.keys())
    return render(request, "blog/index.html",{
        "blogs":blog_titles 
    })
def blogs_n(request, blog_title):
        
    blog_titles = list(blogs.keys())
    if blog_title >= 1 and blog_title <= len(blog_titles):
        redirect_path = reverse("blog-slug",args=[blogs[blog_title]])
        return HttpResponseRedirect(redirect_path)
    else:
        raise Http404()

def blogs_s(request, blog_title):
    if blog_title in blogs.keys():
        return render(request, "blog/blog_article.html", {
            "content": blogs[blog_title],
            "header": blog_title
        })
    else:
        raise Http404()
