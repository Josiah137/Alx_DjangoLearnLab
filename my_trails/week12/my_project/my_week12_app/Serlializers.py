from rest_framework import serializers
from .models import Book
from datetime import date  # Import the date class

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__' # this is to make all list to be displayed on the fields (you can also list speific fields)

    # Define the custom field to be calculated .......to add new feilds in the json(not on model). and on the name of the fieild there will be  a method
    days_since_creation = serializers.SerializerMethodField()
    
    # This method/func calculates the number of days since a cetain book publication if you want to
    # calc the days since creation  you need to mdify the model sinply adding created_at field to hold the time of creatiion with model method "models.DateTimeField(auto_now_add=True)" keza esun ezi gar metkem insteade of the publication method malet new
    # you can find a adetail note on your notion week 12(related to wk 12 of alx)
    def get_days_since_creation(self, obj): # it recives the object(book)
        delta = date.today() - obj.published_date
        return delta.days
    
    