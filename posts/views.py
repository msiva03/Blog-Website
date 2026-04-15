from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from .models import Post, User_details
from django.shortcuts import get_object_or_404
from .forms import UserForm

# Create your views here.
dictionary=[{
    "id": 1,
    "name" : "Let’s Explore Python",
    "content": "Python is a programming language used for many purpose"
},
{
    "id": 2,
    "name": "Let’s Explore Javascript",
    "content": "Javascript is a programming language used for web development"
},
{
    "id": 3,
    "name": "Let’s Explore Java",
    "content": "Java is a programming language used for building enterprise applications"
}
]

def home(request):
    all_posts = Post.objects.all()
    print(all_posts)
    return render(request, "posts/home.html", {"posts": dictionary})

def post_detail(request, id):
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        raise Http404()
    
    return render(request, "posts/post.html", {"post": post})


def google(request, id):
    url = reverse("post", args=[id])
    return HttpResponseRedirect(url)

def form(request):
    if request.method == "POST":
        f = UserForm(request.POST)
        if f.is_valid():
            # name = f.cleaned_data["name"]
            # mail = f.cleaned_data["mail"]
            # contact_number = f.cleaned_data["contact_number"]
            # bio = f.cleaned_data["bio"]
            # user = User_details.objects.create(name=name, mail=mail, contact_number=contact_number, bio=bio)
            # user.save()
            f.save()
            return redirect("form")   # redirect to same page
    else:
        f = UserForm()

    return render(request, "posts/form.html", {"form": f})

def data(request):
    all_data = User_details.objects.all()
    return render(request, "posts/all_data.html", {"all_data": all_data})


def set_cookie_view(request):
    response = HttpResponse("Cookie Set")
    name = request.session['name'] = 'Siva'
    request.session.set_expiry(5)
    return HttpResponse(f"Name: {name}")

def get_cookie_view(request):
    username = request.COOKIES.get('username')
    return HttpResponse(f"Hello {username}")

def delete_cookie_view(request):
    response = HttpResponse("Cookie Deleted")
    request.session.flush()
    request.session.clear_expired()
    return response
