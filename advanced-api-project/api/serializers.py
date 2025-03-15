from rest_framework import serializers
from api.models import Book, Author

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
    
    def validate(self, data):
        if len(data['title']) < 5:
            raise serializers.ValidationError("Title must be at least 5 characters long.")
        return data
    
class AuthorSerializer(serializers.ModelSerializer):
    name = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = "__all__"

    def validate(self, data):
        if len(data['name']) < 5:
            raise serializers.ValidationError("Name must start with a caps.")
        return data