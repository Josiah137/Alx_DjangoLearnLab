from django.urls import path


# from . import views # i can use this but it make me call them like views.display_dep.as_view()  too long
from .views import company_deps_welcome, display_dep
urlpatterns =[
    path('', company_deps_welcome, name="our_departments_landing"), 
    path('list/', display_dep.as_view(), name="department_list"),
]

# the name we have set there help us to call them when rendering