from django.shortcuts import render ,HttpResponse,redirect

# Create your views here.

def home(request):
    return render(request, 'accounts/home.html')

def login_redirect(request):
    return redirect('/account/login/')