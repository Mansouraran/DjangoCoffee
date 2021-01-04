from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.
def index(request):
    if request.method == "POST":
        # do stuff
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        # send mail
        send_mail(
        email,#from mail
        message,#message
        name,#subject
        ['mansoor.salari2021@gmail.com'],#to mail
        fail_silently=False,
        )

        return render (request,'index.html',{'name':name})
    #return the page
    else:
        return render (request,'index.html',{})
