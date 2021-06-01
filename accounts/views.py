from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import  auth
from django.contrib.auth.decorators import login_required
from django.db.models.query_utils import DeferredAttribute
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm


def logout(request):
    auth.logout(request)
    return redirect("/")

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request,"invalid credentials")
            return redirect("login")
    else:
        return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        date_of_birth = request.POST['date_of_birth']
        phone_number = request.POST['phone_number']
        national_id = request.POST['national_id']
        position = request.POST['position']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                 messages.info(request,'Email Taken')
                 return redirect('register')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password =password1,date_of_birth=date_of_birth,phone_number=phone_number,national_id=national_id,position=position)
                user.save()
                return redirect("login")
        else:
            messages.info(request,'Password Not Matching')
            return redirect('register')
        return redirect('/')
    else:
        return render(request,'register.html')




@login_required
def profile(request):
    current_user= request.user
    search = current_user.username
    employees = User.objects.all().filter(username__icontains=search)
    context = {'search':search,'employees':employees}
    return render(request,'profile.html',context)

@login_required  
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('/')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})
    
