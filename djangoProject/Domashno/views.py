from django.db.models import Q
from django.shortcuts import render, redirect
from .models import BlogPost, Author
from datetime import datetime
from .forms import BlogPostForm, AddingBlockedUsersForm


# Create your views here.
def posts(request):
    if request.user.is_authenticated:
        authorUser = Author.objects.get(user=request.user)
        queryset = BlogPost.objects.filter(~Q(author=authorUser)).filter(~Q(author__user__in=authorUser.blockedUser.all()))
        context = {"posts": queryset, "date": datetime.now().date()}
        return render(request, "posts.html", context=context)
    else:
        return redirect("/admin")


def addBlogPost(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blogpost = form.save(commit=False)
            blogpost.author = Author.objects.get(user=request.user)
            blogpost.date = datetime.now()
            blogpost.lastChange = datetime.now()
            blogpost.save()
            return redirect("posts")
        else:
            print(form.is_valid())
            print(form.errors)
    context = {"date": datetime.now().date(), "form": BlogPostForm}
    return render(request, "addpost.html", context=context)


def profile(request):
    authorUser = Author.objects.get(user=request.user)
    queryset = BlogPost.objects.filter(author=authorUser)
    context = {"date": datetime.now().date(), "user": request.user, "posts": queryset, "author": authorUser}
    return render(request, "profile.html", context=context)


def blockedUsers(request):
    authorUser = Author.objects.get(user=request.user)
    queryset = authorUser.blockedUser.all()
    if request.method == "POST":
        form = AddingBlockedUsersForm(request.POST, instance=Author.objects.get(user=request.user))
        if form.is_valid():
            form.save()
            return redirect("blockedUsers")
        else:
            print(form.is_valid())
            print(form.errors)
    context = {"blocked": queryset, "user": request.user, "form": AddingBlockedUsersForm}
    return render(request, "blockedUsers.html", context=context)
