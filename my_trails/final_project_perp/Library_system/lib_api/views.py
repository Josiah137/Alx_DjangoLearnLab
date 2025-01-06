from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import ModelViewSet
from .models import Book, Author, Genre
from .Serializator import AuthorSerializer, GenreSerializers, BookSerializers
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
# from rest_framework.authentication import TokenAuthentication
from rest_framework.authentication import BasicAuthentication

#settting app all instances and their respective serilizer
# permission class is the one that block users from acesssing certain content if we reove that everyone has acess for everything. so sensetive contents has to be protected
class Bookviewset(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
    authentication_classes = [BasicAuthentication]
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
    permission_classes = [IsAuthenticatedOrReadOnly] # we made it like users can add teh gener of a book only if they are authic/knowen user(loged in)