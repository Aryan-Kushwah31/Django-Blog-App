from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required 
from django.core.paginator import Paginator
from .forms import PostForm, UserForm, LoginForm
from .models import Posts

def home(request):
    posts = Posts.objects.all().order_by("-date")
    
    page_number = request.GET.get("page")
    paginator = Paginator(posts, 6)
    page_obj = paginator.get_page(page_number)
    context = {'posts':posts, 'page_obj':page_obj}
    return render(request, 'home.html', context)

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        print("Method is Post")
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(username, password, "After Validation")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                print("Logged in after auth....Redirectind")
                return redirect('home')
            else:
                return HttpResponse("Not a User Sign Up")
    return render(request, 'login.html')

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        print(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.filter(email=email).first()
            if user:
                messages.error(request, "User Already Exist")
                return redirect("home")
            else:
                user = User.objects.create_user(username=first_name, email=email, password=password)
                user.last_name = last_name
                user.save()
                messages.success(request, "Signed Up Successfully.")
                return redirect("home")
    return render(request, 'signup.html')

def logout_view(request):
    logout(request)
    return redirect("home")

@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            post = Posts(title=title, content=content)
            post.save()
            messages.success(request, 'Posted Successfully')
            return redirect("home")
    return render(request, 'create.html')

def content(request, pk):
    posts = Posts.objects.get(pk=pk)
    context = {'posts':posts}
    print(posts.pk)
    return render(request, 'content.html', context)


def delete_view(request, pk):
    post = Posts.objects.get(pk=pk)
    post.delete()
    messages.success(request, 'Deleted Successfully')
    return redirect("home")