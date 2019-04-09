from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm, NeighborhoodForm, ProfileForm, PostForm, BusinessForm, PoliceForm, HealthForm
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Profile, Post, Business, Police, Health
from django.contrib.auth.models import User
@login_required(login_url='/accounts/login/')
def welcome(request):
    user=request.user
    profile=Profile.objects.get(user=user)
    posts = Post.objects.filter(neighborhood=profile.neighborhood)
    hcenters=Health.objects.filter(neighborhood=profile.neighborhood)
    polices = Police.objects.filter(neighborhood=profile.neighborhood)
    businesses=Business.objects.filter(neighborhood=profile.neighborhood)
    return render(request, 'welcome.html',{"posts":posts,"hcenters":hcenters,"polices":polices,"businesses":businesses})

@login_required(login_url='/accounts/login/')
def posts(request,post_id):
    post = Post.objects.get(id = post_id)
    return render(request,"info.html", {"post":post})

@login_required(login_url='/accounts/login/')
def myProfile(request,id):
    user = User.objects.get(id = id)
    profiles = Profile.objects.get(user = user)
    posts = Post.objects.filter(user = user).all()
    form = ProfileForm()
   
    return render(request,'my_profile.html',{"profiles":profiles,"user":user,"posts":posts,"form":form})



def profile(request):
    current_user = request.user
    profile=Profile.objects.get(user=current_user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()

        return redirect(welcome)

    else:
        form = ProfileForm()
    return render(request, 'profile.html', {"form": form,"user":current_user,"profile":profile})

def neighborhood(request):
    current_user = request.user
    if request.method == 'POST':
        form = NeighborhoodForm(request.POST, request.FILES)
        if form.is_valid():
            neighborhood = form.save(commit=False)
            neighborhood.user = current_user
            neighborhood.save()

        return redirect(welcome)

    else:
        form = NeighborhoodForm()
    return render(request, 'neighborhood.html', {"form": form})

def business(request):
    current_user = request.user
    if request.method == 'POST':
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            business = form.save(commit=False)
            business.user = current_user
            business.save()

        return redirect(welcome)

    else:
        form = BusinessForm()
    return render(request, 'business.html', {"form": form})

def police(request):
    current_user = request.user
    if request.method == 'POST':
        form = PoliceForm(request.POST, request.FILES)
        if form.is_valid():
            police = form.save(commit=False)
            police.user = current_user
            police.save()

        return redirect(welcome)

    else:
        form = PoliceForm()
    return render(request, 'police.html', {"form": form})

def health(request):
    current_user = request.user
    if request.method == 'POST':
        form = HealthForm(request.POST, request.FILES)
        if form.is_valid():
            health = form.save(commit=False)
            health.user = current_user
            health.save()

        return redirect(welcome)

    else:
        form = HealthForm()
    return render(request, 'health.html', {"form": form})



def post(request):
    current_user = request.user
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
        return redirect(welcome)
    else:
        form = PostForm()
    return render(request, 'post.html', {"form": form})

def search_results(request):

    if 'business' in request.GET and request.GET["business"]:
        search_term = request.GET.get("business")
        searched_businesses = Business.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"businesses": searched_businesses})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

# Create your views here.