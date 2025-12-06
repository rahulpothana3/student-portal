from django.shortcuts import render
from django.http import JsonResponse

def home(request):
    return render(request, 'base.html')
def login(request):
    return render(request, 'login.html')
def signup(request):
    return render(request , 'signup.html')

def submitform(request):
    if request.method=="POST":
        data={
            "email":request.POST.get("email"),
            "password":request.POST.get("password")
        }
   # return JsonResponse(data)     
    return render(request, "form.html", data)

def registerinfo(request):
    if request.method=="POST":
        data={
            "fullname":request.POST.get("fullname"),
            "email":request.POST.get("email"),
            "studentid":request.POST.get("studentid"),
            "department":request.POST.get("department"),
            "password":request.POST.get("password"),
            "confirmpassword":request.POST.get("confirmpassword"),

        }
    return render(request, 'signupinfo.html', data)

# Create your views here.
