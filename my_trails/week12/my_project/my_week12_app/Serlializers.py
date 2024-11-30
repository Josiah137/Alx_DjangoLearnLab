from rest_framework import serializers
from .models import Book
from datetime import date  # Import the date class

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    # Define the custom field to be calculated
    days_since_creation = serializers.SerializerMethodField()
        # This method calculates the number of days since creation
    def get_days_since_creation(self, obj):
        delta = date.today() - obj.published_date
        return delta.days
    