from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from blogapp.models import Blogs
from blogapp.forms import AddBlogForm,UpdateBlogForm
from django.contrib.auth.decorators import login_required

@login_required
def home_view(request):
    return render(request,"blogapp/home.html")

def user_register_view(request):
    form=UserCreationForm()
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/login/")

    return render(request,"blogapp/register.html",{"form":form})

@login_required
def list_of_blogs(request):
    data=Blogs.objects.all()
    return render(request,"blogapp/list.html",{"data":data})

@login_required
def add_new_blog_view(request):
    form=AddBlogForm()
    if request.method=="POST":
        form=AddBlogForm(request.POST,request.FILES)
        if form.is_valid():
            obj=form.save(commit=False)  
            obj.user=request.user
            form.save() 
            return redirect("/blogs/list/")
    return render(request,"blogapp/add.html",{"form":form})

@login_required
def detail_view(request,id):
    obj=Blogs.objects.get(pk=id)
    return render(request,"blogapp/detail.html",{"obj":obj})

@login_required
def blog_update_view(request,id):
    obj=Blogs.objects.get(pk=id)
    form=UpdateBlogForm(instance=obj)
    if request.method=="POST":
        form=UpdateBlogForm(request.POST,request.FILES,instance=obj)
        if form.is_valid():
            form.save()
            return redirect("/blogs/list/")
    return render(request,"blogapp/update.html",{"obj":obj,"form":form})

@login_required
def blog_delete_view(request,id):
    obj=Blogs.objects.get(pk=id)
    obj.delete()
    return redirect("/blogs/list/")


