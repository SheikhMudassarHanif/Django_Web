from django.shortcuts import render
from regiterformapp.forms import UserForm,UserProfileInfoForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def display_home(request):
    return render(request,'homepage.html')

@login_required
def special(request):
    return HttpResponse("YOU are LOGGED IN")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))

def display_signup(request):
    registered=False;

    if request.method=='POST':
        obj_user=UserForm(data=request.POST)
        obj_profile=UserProfileInfoForm(data=request.POST)

        if obj_user.is_valid() and obj_profile.is_valid():
            user=obj_user.save()
            user.set_password(user.password)
            user.save()

            profile=obj_profile.save(commit=False)
            profile.user=user

            if 'picture' in request.FILES:
                profile.picture=request.FILES['picture']

                profile.save()
                registered=True

        else:
            print(form.errors)
    else:
        obj_user=UserForm()
        obj_profile=UserProfileInfoForm()



    return render(request,'signup.html',{'user_form':obj_user,'profile_form':obj_profile,'registered':registered})





#
# def display_login(request):
#     if request.method=='POST':
#     objusername=request.POST.get('username') #this get is used because in our html we used label username
#     objpwd=request.POST.get('password')
#     user=authticate(username=username,password=password)
#
#     if user:
#         if user.is_active:
#             login(request,user)
#             return HttpResponseRedirect(reverse('homepage'))
#         else:
#             return HttpResponse("ACCOUNT NOT ACTIVE")
#     else:
#         print("someone tired to login and failed")
#         print("username: {} and password {}".format(username,password))
#         return HttpResponse("invalid login details")
#
#     else:
#         return render(request,'login.html',{})


def display_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # get the value from the 'username' input field
        password = request.POST.get('password')  # get the value from the 'password' input field
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active==True:
                login(request,user)
                return HttpResponseRedirect(reverse('homepage'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("someone tried to login and failed")
            print("username: {} and password: {}".format(username, password))
            return HttpResponse("Invalid login details")
    else:
        return render(request, 'login.html', {})
#
# def display_login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')  # get the value from the 'username' input field
#         password = request.POST.get('password')  # get the value from the 'password' input field
#         user = authenticate(username=username,password=password)
#
#         if user:
#
#                 if user.is_active:
#                 login(request, user)
#                 return HttpResponseRedirect(reverse('homepage'))
#             else:
#                 return HttpResponse("ACCOUNT NOT ACTIVE")
#         else:
#             print("someone tried to login and failed")
#             print("username: {} and password: {}".format(username,password))
#             return HttpResponse("Invalid login details")
#     else:
#         return render(request, 'login.html', {})
