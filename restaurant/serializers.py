from django.contrib.auth.models import User
from rest_framework import serializers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class MenuItemSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=200)
    price = serializers.DecimalField(max_digits=6, decimal_places=2)
    menu_item_description = serializers.CharField(max_length=1000, default='') 

class BookingSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    first_name = serializers.CharField(max_length=200)
    reservation_date = serializers.DateField()
    reservation_slot = serializers.IntegerField(default=10)