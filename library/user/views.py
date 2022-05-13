from urllib import request
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login as login_, logout as logout_
from django.views import View

from user.forms import CustomUserCreationForm, LoginForm


# request.POST =====> queryDict ====> data form
# request.GET =====> queryDict ====> url query parameters  ex: /salam/?name=a&age=12  

def login(request):
    if request.method == "GET":
        return render(request, "user/login.html", {})
    elif request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user:
            login_(request, user)
            return redirect("/")
        return HttpResponse("merc")


def logout(request):
    logout_(request)
    return redirect("/")

class Login(View):
    def get(self, request):
        if request.user.is_authenticated:
            # logout(request)
            return redirect('/')
        form = LoginForm()
        context = {
            'form': form,
        }
        return render(request, 'user/login.html', context)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login_(request, user)
                return redirect('/')
            else:
                return redirect('login')

                
class SignUp(View):
    
    def get(self, request):
        form = CustomUserCreationForm()
        context = {
            'form': form
        }
        return render(request, 'user/signup.html', context)

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

        context = {
            'form': form
        }
        return render(request, 'user/signup.html', context)

