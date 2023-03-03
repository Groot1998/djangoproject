from django.shortcuts import render,redirect
from django.contrib import messages
from  django.http import HttpResponse
from . forms import RegisterForm
from . models import Register
# Create your views here.
def hello(request):
    return HttpResponse("welcome to project9")

def index(request):
    name='try'
    return render(request,'index.html',{'data':name})
# def signup(request):
#     form=RegisterForm()
#     return render(request,'signup.html',{'form':form})


def signup(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['Name']
            age=form.cleaned_data['Age']
            place=form.cleaned_data['Place']
            email=form.cleaned_data['Email']
            password=form.cleaned_data['Password']
            confirmpassword=form.cleaned_data['ConfirmPassword']
            user=Register.objects.filter(Email=email).exists()

            if user:
                messages.warning(request,'email already exits')
                return redirect('/signup')
            elif password!=confirmpassword:
                messages.warning(request,'password mismatch')
                return redirect('/signup')
            else:
                tab=Register(Name=name,Age=age,Place=place,Email=email,Password=password)
                tab.save()
                messages.success(request,'data entered')
                return redirect('/')

    else:
        form=RegisterForm()
    return render(request,'signup.html',{'form':form})