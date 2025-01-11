from django.shortcuts import render

# Create your views here.
""" this is a continuation from mytrails week12 lib_api app (or another form of it )"""
from rest_framework.viewsets import ModelViewSet
from .models import Book, Author, Genre
from .Serializator import AuthorSerializer, GenreSerializers, BookSerializers
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
# from rest_framework.authentication import BasicAuthentication

#settting app all instances and their respective serilizer
# permission class is the one that block users from acesssing certain content if we reove that everyone has acess for everything. so sensetive contents has to be protected
class Bookviewset(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
    authentication_classes = [TokenAuthentication] # this is redendency. since we already have mentioned it globally. weye unless we have set diffrent auth types globally and we are definfinf w/h one to use for this view  
    permission_classes = [IsAuthenticated] # this line set the permission for the view to be seen by authticated users only and we set
                                           # what kinda of authtication we meant on z above, basic Auth. it can also be other type like token auth
                                         
    def get(self, request):
        return Response({"message": "You have access!"})


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated, IsAdminUser] # only admins can acsses this now(get, post )

class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializers
    permission_classes = [IsAuthenticatedOrReadOnly] # we made it like users can add the gener of a book only if they are authic/knowen user(loged in ones)


# all the above is to over ride by the way. globally in settings i have given  authentication for every view with TokenAuthentication
# and permission to auth. so coming here and saying:   
"""
authentication_classes = [TokenAuthentication] 
permission_classes = [IsAuthenticated]
"""
# is a redendency if we leave it empety by default they have this auth and permission.
# unless we have multiple auth declared globally.  
# the permssion we set on the actual code above is not redendencey the defualt is is authticated and we are overridding that.