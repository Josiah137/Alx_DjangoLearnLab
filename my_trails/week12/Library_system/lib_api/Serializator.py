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

    # creating field level validation ... just to set charactr limimt for each gener 
            # field level validation syntax: vlidate_<fildname>
    # def validate(self, attrs):
        #  return super().validate(attrs)
    def validate_name(self, value):
        if len(value) > 25:
            raise serializers.ValidationError("gener name can not be morethan 25 characters")
        return value
    # def genre_count():    


class BookSerializers(serializers.ModelSerializer):
    author = AuthorSerializer() 
    genre = GenreSerializers(many=True)

    class Meta:
        model = Book
        fields =  "__all__"

    # object(instance) level validation  .... just set some limit for the amount of geners a book can have
    # it is defined here (intade of on the Genere class) because we are not planning to set control on a single genere instance but total gener a book may have so we came here 
    def validate(self, data):
        if len(data[Genre]) > 5:
            raise serializers.ValidationError("a book can't have more than 5 geners \nplease try again later")
        return data







        # 
        # # def validate(self, attrs):
        #  return super().validate(attrs)