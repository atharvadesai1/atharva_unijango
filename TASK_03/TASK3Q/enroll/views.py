
from cgitb import html
from multiprocessing import context
from unicodedata import name
from urllib import response
from django.shortcuts import render
import requests
from. forms import usernametw
from django import forms
from django.http import HttpResponse 
# import templates
# def task3dj(request):
#     obj = Student()
#     return render(request,'enroll/userregistration.html',{'form':obj})

def task3dj(request):
    if request.method == "POST":
        id = int  
        id = request.POST.get('xyz')
        user_id = int

        url = "https://twitter154.p.rapidapi.com/user/id"

        querystring = {"user_id":id}

        headers = {
            "X-RapidAPI-Key": "2c4de38ab5msh5c0f5c2f2daded8p1d352bjsn8a66c731188e",
            "X-RapidAPI-Host": "twitter154.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        print(response.text)
        return HttpResponse(response.text)
    return render(request, 'enroll/pirate.html',{'fill':'Twitter'})    
        
        

# def man(request):
#     c = usernametw()
#     return render(request, 'enroll/userregistration.html',{'form':c})

# def user(request):
#     user_twitter = 'narendramodi'
#     return render(request, 'enroll/pirate.html', {"fill": "Twitter"} )    


    
    
    
