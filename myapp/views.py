from django.shortcuts import render

# Create your views here.
name="PYSPIDERS"
email="pyspiders@gmail.com"
phno="9966206473"
def index(request):
    return render(request,"home.html",{'name':name})
def courses(request):
    return render(request,"courses.html",{'name':name})
def aboutus (request):
    return render(request,"aboutus.html",{"name": name,"email":email,"phno":phno})
def enquiry (request):
    return render(request,"enquiry.html",{"name": name,"email":email,"phno":phno})
def batches(request):
    return render(request,"batches.html",{"name": name,"email":email,"phno":phno})