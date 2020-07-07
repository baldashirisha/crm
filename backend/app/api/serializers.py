from rest_framework import serializers
from app.models import User, Contact, Notes

# class rolesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = roles
#         fields = '__all__'

# class user_statusSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = user_status
#         fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = '__all__'