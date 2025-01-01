from django.shortcuts import render,redirect
from django.http import JsonResponse
 # from .models import Conversion
from .models import Convert,User,conversion
from word2number import w2n
import json
from django.contrib import messages
from .forms import RegistrationForm, LoginForm
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.sessions.models import Session
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required

# # Create your views here.
# # def hello(request):
# #     return HttpResponse("hello")


def print(request):
     return render(request,'index.html')


# def login(request):
#     return render(request,'login.html')

# def register(request):
#     return render(request,'register.html')


def convert(request):
    if 'user_id' not in request.session:           # session chechking user id
        return JsonResponse({"error": "Please login"}, status=401)

    if request.method == "POST":
        data = json.loads(request.body)
        text= data.get('text','').strip()
        if not text:
            return JsonResponse({"error":"input cannot be empty"},status=400)
        
        try:
            result=w2n.word_to_num(text)
            conversions=Convert.objects.create(text_input=text,number_result=result)
            return JsonResponse({"result":result})
        except ValueError:
            return JsonResponse({"error":"invalid input"},status=400)
        
    return JsonResponse({"error":"invalid mathod"},status=405)
    


# Registration view
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create(username=username, email=email, password=password)
            user.save()

            

            messages.success(request, 'Registration successful,log in...')
            return redirect('login')  
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})

# Login view
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            
            try:
                user = User.objects.get(username=username)
                if user.password == password: 
                    request.session['user_id'] = user.id           #create a session
                    messages.success(request, 'login successful')
                    return redirect('index')  
                else:
                    messages.error(request, 'Incorrect password.')
                    return redirect('login')
            except User.DoesNotExist:
                messages.error(request, 'User does not exist.')
                return redirect('login')
    
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

# logout view 

def logout(request):
    if 'user_id' in request.session:
        del request.session['user_id']
    messages.success(request, 'You have been logged out.')
    return redirect('login')


