from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# from .models import 

def landing(request):
    return HttpResponse("WELLCOME to our library. you can put studyrooms/<the study room you want>")
def room1 (request):
    return HttpResponse("this is an HttpResponse <br> .....  Hmmm, btw this is room 1 :)  <br><br> in a wrong room? here is <a href='http://127.0.0.1:5000/studyrooms/room2/'>room 2</a>   <br><br> you can see that it is working as a normal html file but since it is an html response (just 1 line), you can't do much here, it is limiting")

#how can we rended and html page upon a request?
def room2(request):
    return render(request, 'index.html')

