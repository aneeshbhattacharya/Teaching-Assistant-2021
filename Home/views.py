from django.shortcuts import redirect, render
from cryptography.fernet import Fernet

from .models import UserDetails


# Create your views here.

def homePage(request):

    if(request.method == 'POST'):

        email = request.POST.get('number1')
        password = request.POST.get('number2')

        try:
            object = UserDetails.objects.get(email = email)
        except:
            object = None
        
        if(object==None):
            context = {
                'message': "Email Does Not Exist"
            }
            return render(request,"home.html",context)

        if(password == object.password):
            return render(request,"dashboard.html",{})
        else:
            return redirect("/")

    else:
        return render(request,"home.html",{})

def signUpPage(request):

    if(request.method == 'POST'):
        email = request.POST.get('email')
        password = request.POST.get('password')
        passwordVerif = request.POST.get('passwordVerif')

        if(password == passwordVerif):
            key = Fernet.generate_key()
            f = Fernet(key)
            password = bytes(password,'utf-8')
            token = f.encrypt(password)
            UserDetails.objects.create(email=email,password=token, key = key)
            return redirect("/")
        
        else:
            return redirect("/sign-up")

    else:
        return render(request,"signUp.html",{})

def dashBoard(request):

    return render(request,"dashboard.html",{})


    