from cgitb import text
from multiprocessing import context
from unicodedata import name
from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import feature
# Create your views here.

def index(request):
    #pass
    #*********
    #return HttpResponse('<h1>Hello Hello </h1> ')
    #***********
    #return render(request, 'index.html')
    #***********
    #name = 'joshua'
    #return render(request, 'index.html', {'name': name})
    #*************
    '''context = {

        'name': 'Oluwaseyi',
        'age' : '25',
        'Nationality' : 'Nigeria',
        'Level' : 'PhD',
    }'''
   # return render(request, 'index.html',context)
   #*********** setting and fetching data with an object of a class*****************
    '''feature1 = feature()
    feature2 = feature()
    feature3 = feature()
    feature4 = feature()

    feature1.name = 'Relaiable'
    feature1.id = 0
    feature1.details = 'our product is very Reliable'

    feature2.id = 1
    feature2.name = 'Usable'
    feature2.details = 'Usability of our product is sure'

    feature3.name = 'Durable'
    feature3.id = 0
    feature3.details = 'The Durability of our products cannot be compared'

    features = [feature1, feature2, feature3]

    return render(request, 'index.html', {'features': features})'''
#*****************using db instead*******************
    features = feature.objects.all()
    return render(request, 'index.html', {'features': features})

def register (request):
    if request.method == 'POST':
       # email = request.POST[email]
        username = request.POST[username]
        password = request.POST[password]
        password2 = request.POST[password2]
        
        if password == password2:
            if User.objects.filter(email=email).exits():
                messages.info(request, 'email in usee')
                return redirect('register')
            elif User.objects.filter(username=username).exits():
                messages.info(request, 'UserName already in usee')
                return redirect('register.html')
            else: 
                user = User.objects.create_user(username = username, email = email, password = password)
                User.save
            return redirect('login')
        else: 
            messages.info(request, 'wrong password')
            return redirect('register')
    else:
        return render(request, 'register.html')

#*******creating a function for counter here

def josh (request):
    
    text = request.POST['text']
    wordamount = len(text.split(' '))
    numWord = str(wordamount) + "from josh method"
    
    return render(request, 'counter.html', {'text': numWord})
    
def counter (request):
   
    text = request.POST['text']
    wordamount = len(text.split(' '))
    context = {

        'name': 'Oluwafunmilayo temi',
        'age' : '25',
        'Nationality' : 'Nigeria',
        'Level' : 'PhD',
        'text' : wordamount,
    }
    return render(request, 'index.html',context)