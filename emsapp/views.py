from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import  auth
from django.contrib.auth.decorators import login_required
from .models import User,Leave
from django.db.models.query_utils import DeferredAttribute
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .forms import Leaveform

# Create your views here.
def home(request):
    return render(request,'base.html')



def searchbar(request):
    search = request.GET['query']
    employees = User.objects.all().filter(username__icontains=search)
    context = {'search':search,'employees':employees}
    return render(request,'searchbar.html',context)


    
@login_required    
def leave_request(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = Leaveform(request.POST)
            if form.is_valid():
                user = form.save()
            return redirect('/')
        form = Leaveform
        return render(request,'leave.html',{'form':form})

@login_required
def leave_status(request):
    current_user= request.user
    search = current_user.username
    employees = Leave.objects.all().filter(username__username__icontains=search)
    context = {'search':search,'employees':employees}
    return render(request,'leave_status.html',context)