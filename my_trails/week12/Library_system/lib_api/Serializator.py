from rest_framework import serializers
from .models import Author, Genre, Book

#making nested cerialization

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["name"] # you can list them like this or say __all__

class GenreSerializers(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"

    # creating field level validation ... just to set some limit for the amount of geners a book can have
    # field level validation syntax: vlidate_<fildname>
    # def validate(self, attrs):
        #  return super().validate(attrs)
    def validate_name(self, value):
        if len(value) > 5:
            raise serializers.ValidationError("a book can't have more than 5 geners \nplease try again later")
        return value

class BookSerializers(serializers.ModelSerializer):
    author = AuthorSerializer() 
    genre = GenereSerializers()

    class Meta:
        model = Book
        fields =  ["name, published_date, iSBN_number"]    # we can not use "__all__" here b/se we are specifing how some of the fields has to be 
        #sreilized(author, gener) and if we use all we are creating conflicts since we are telling the fiilds to be serilized in two diffrent ways 