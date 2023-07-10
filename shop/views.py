import json
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core import serializers


# Create your views here.
# @login_required(login_url="login")
def home(request):
    items = Item.objects.all()

    # items_json = serializers.serialize('json', items)
    return render(request, "home.html", {"items": items})


@login_required(login_url="login")
def item_detail(request, pk):
    item = Item.objects.get(id=pk)
    flag = True
    if item.owner == request.user:
        flag = False
    for i in item.users.all():
        if i == request.user:
            flag = False
    print(flag)
    if request.method == "POST":
        item.users.add(request.user)
        item.save()
        return redirect("/")
    return render(request, "item_detail.html", {"item": item, "flag": flag})


# def getItems(request):
#     items = Item.objects.all().values()
#     data = list(items)
#     return JsonResponse({"items": data}, safe=False)

@login_required(login_url="login")
def myItems(request):
    user = request.user
    items = user.owned_items.all()
    context = {
        "user": user,
        "items": items,
    }
    return render(request, "myItems.html", context)

@login_required(login_url="login")
def electronics(request):
    electronic_items = Item.objects.filter(category="Electronics")
    return render(request, "electronics.html", {"items": electronic_items})

@login_required(login_url="login")
def fashion(request):
    return render(
        request, "fashion.html", {"items": Item.objects.filter(category="Fashion")}
    )

@login_required(login_url="login")
def games(request):
    return render(
        request, "games.html", {"items": Item.objects.filter(category="Toys and Games")}
    )

@login_required(login_url="login")
def sports(request):
    return render(
        request,
        "sports.html",
        {"items": Item.objects.filter(category="Sports and Outdoors")},
    )


def signup(req):
    form = UserForm()

    if req.method == "POST":
        form = UserForm(req.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            messages.success(req, "Account was created for " + user.username)
            return redirect("login")

    return render(req, "signup.html", {"form": form})


def loginUser(req):
    if req.method == "POST":
        username = req.POST.get("username")
        password = req.POST.get("password")

        user = authenticate(req, username=username, password=password)

        if user is not None:
            login(req, user)
            return redirect("home")
        else:
            messages.info(req, "username or password is inccorect")
            return render(req, "login.html")
    return render(req, "login.html")


def logoutUser(req):
    logout(req)
    return redirect("login")


@login_required(login_url="login")
def create_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save()
            item.owner = request.user
            item.save()
            return redirect("/")
    else:
        form = ItemForm()
    return render(request, "newItem.html", {"form": form})
