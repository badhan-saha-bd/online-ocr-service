from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
def confirmation(request):
    name = request.POST['Name']
    email = request.POST['Email']
    password = request.POST['Password']
    if name==''or email=='' or password=='':
        return redirect('/authorize')
    else:

        user = User.objects.create_user(username=name,email=email,password=password)
        
        return render(request,'confirmation.html',{'result':'Congratulation! Your Registration Is Complete'})
