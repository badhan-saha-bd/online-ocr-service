from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
def dashboard(request):
    if request.method == 'POST':
        username = request.POST['Name']
        password = request.POST['Password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            return render(request,'dashboard.html')
        else:
            return render(request,'confirmation.html',{'result':'Sorry Login Failed!'})
