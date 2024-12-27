from django.shortcuts import render

# Create your views here.
#---------------------- i could have create this  but instade of having 3 apps i decided to do it all in one and then scale it.
#/////////////// so go to the employees app and u find it all there 

from .models import Departments
from django.http import HttpResponse

# below we wil be settting views some with FCB and some with CPB for you to see. as you know the CBV is most recommend one
# function based views
def company_deps_welcome(request):
    return (render(request, 'departments_Home.html'))

def landing(request):
    #return HttpResponse("hi, there! welcome!! <br> this is the landing page btw <br> i could have put the links here or make it rendered from http ")
    return (render(request, 'index.html'))

# class based views
from django.views.generic import ListView

class display_dep(ListView):
    model = Departments
    template_name = "department_list.html"
    context_object_name = "our_department_list"


