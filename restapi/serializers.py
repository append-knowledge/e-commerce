from rest_framework.serializers import  ModelSerializer
from rest_framework import serializers
from user.models import MyUser,Order,Product

class SignUpserializer(ModelSerializer):
    class Meta:

        model=MyUser
        fields=['username','email','password']

        def create(self, validated_data):
            return MyUser.objects.create_user(username=validated_data['username'], password=validated_data['password'],
                                              email=validated_data['email'])


class SigninSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class ProductSerializer(ModelSerializer):
    class Meta:
        model=Product
        fields=['product_name','price','stock','image']

class OrderSerializer(ModelSerializer):
    class Meta:
        model=Order
        fields=['product','user','address','phone_number']
