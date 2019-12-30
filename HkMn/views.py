from django.shortcuts import render
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth import models
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, render_to_response
from django.contrib.auth.models import User
from HkMn.models import team, wifi, submissions, judges


def home(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            loguser=request.user
            if str(loguser)[0] == 't':
                try:
                    teamprofile = team.objects.get(username=loguser)
                except team.DoesNotExist:
                    teamprofile = None
                if teamprofile==None or teamprofile.count==0:
                    return redirect('/teamedit/')

                return render(request, 'HkMn/dashboard.html',{ 'user' : user })
            elif str(loguser) == 'cafeteria' :
                return render(request, 'HkMn/cafe_dashboard.html',{ 'user' : user })
            else: 
                return redirect('/judgescore/')


        else:
            return render(request,"HkMn/login.html",{ 'message': 'true'})


    else:
        if not request.user.is_authenticated:
            return redirect('/login/')
        else:
            loguser = request.user
            if str(loguser)[0] == 't':
                try:
                    teamprofile = team.objects.get(username=loguser)
                except team.DoesNotExist:
                    teamprofile = None
                if teamprofile==None or teamprofile.count==0:
                    return redirect('/teamedit/')

                return render(request, 'HkMn/dashboard.html')
            elif str(loguser) == 'cafeteria' :
                return render(request, 'HkMn/cafe_dashboard.html')
            else: 
                return redirect('/judgescore/')
            return render(request, 'HkMn/home.html')


def mylogout(request):
    logout(request)
    request.session['user']=''
    return render(request, 'HkMn/logout.html')


def teamdash(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    else:
        if request.method == 'POST':
            loguser = request.user
            try:
                teamprofile = team.objects.get(username=loguser)
            except team.DoesNotExist:
                teamprofile = None
            if teamprofile == None :
                use = team.create(loguser)
                use.name1=request.POST['name1']
                use.name2=request.POST['name2']
                use.name3=request.POST['name3']
                use.name4=request.POST['name4']
                use.phone=request.POST['phone']
                print("XDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDd",str(use.phone))
                use.count=1
                use.save()
                return redirect('/home/')
        
            
            

            return redirect('/home/')

        else:
            loguser = request.user
            try:
                teamprofile = team.objects.get(username=loguser)
            except team.DoesNotExist:
                teamprofile = None
            if teamprofile == None :
                
                return render(request, 'HkMn/user.html',{ 'user' : loguser })
            else:
                loguser = request.user
                return render(request, 'HkMn/user1.html',{ 'user' : loguser , 'tp' : teamprofile})

def wififetch(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    else:
        loguser = request.user
        teamwifi = wifi.objects.get(username=loguser)
        print(str(teamwifi.pawd), "looooooooooooooooooooooooooooooooooool")
        return render(request, 'HkMn/wifi.html',{ 'user' : loguser , 'wifi' : teamwifi })

def judgescore(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    else:
        if request.method == 'POST':
            loguser = request.user
            subna = request.POST['subna']
            subn = submissions.objects.get(sublink = subna)
            print("ianfoiwnfoiqnqoifonqofoiqfqoifnqofnqoifnoinoiqoifno", subn)
            try:
                datasub = judges.objects.get(username = loguser , tname = subn)
            except judges.DoesNotExist:
                datasub = None
            if datasub == None :
                use = judges.create(loguser)
                use.tname = subn
                use.score=request.POST['score']
                print("XDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDd",str(use.tname))
                use.save()
                return redirect('/home/')
            return redirect('/home/')

        else:
            loguser = request.user
            datasub = submissions.objects.all()
            return render(request, 'HkMn/judge_dashboard.html',{ 'user' : loguser , 'data' : datasub , 'data1' : datasub })
    
    
def submitpjt(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    else:
        if request.method == 'POST':
            loguser = request.user
            sublink = request.POST['sublink']
            print("starting!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            try:
                datasub = submissions.objects.get(username = loguser)
            except submissions.DoesNotExist:
                datasub = None
            if datasub == None :
                use = submissions.create(loguser)
                use.sublink = sublink
                print("XDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDd",str(use.sublink))
                use.save()
                return redirect('/home/')
            print("Did nothing loooooooooooooooooool")
            return redirect('/home/')

        else:
            loguser = request.user
            return render(request, 'HkMn/upload_files.html',{ 'user' : loguser })
    
    
                