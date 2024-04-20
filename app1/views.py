from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import HouseCreateForm, RoomCreateForm
from .models import House, Room

# Create your views here.

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        



    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            print(user)
            return redirect('house')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def house(request):
    if request.method == 'POST':
        form = HouseCreateForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('house_list')
    else:
        form = HouseCreateForm()
    return render(request, 'house_create.html', {'form': form})

def house_list(request):
    houses = House.objects.filter(user=request.user)
    return render(request, 'house_list.html', {'houses': houses})




# def room(request):
#     pass
