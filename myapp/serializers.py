from myapp.models import PoductModel, UserModel
from rest_framework import serializers


class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoductModel
        fields = ['ProductName','ProductPrice','ProductDescription','ProductImage']

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['firstname','username', 'lastname', 'address']
