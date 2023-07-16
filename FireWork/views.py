from django.shortcuts import render
from FireWork.models import contact


# Create your views here.
def index(request):
    return render(request,'index.html')


def signupView(request):
    return render(request,'signup.html')


def Sketches(request):
    return render(request,'Sketches.html')

def Paintings(request):
    return render(request,'Paintings.html')

def Scultptures(request):
    return render(request,'Scultptures.html')

def ColorPencilArt(request):
    return render(request,'ColorPencilArt.html')

def Contact(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        PhoneNumber = request.POST['PhoneNumber']
        message = request.POST['message']
        print(name,email,PhoneNumber,message)
        Contact = contact(name = name, email = email, PhoneNumber = PhoneNumber, message = message)
        Contact.save()
    return render(request,'ContactUs.html')

def AboutUs(request):
    return render(request,'AboutUs.html')

