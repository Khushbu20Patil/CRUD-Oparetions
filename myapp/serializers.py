from myapp.models import PoductModel, UserModel
from rest_framework import serializers


class ProductModelSerializer(serializers.ModelSerializer):
    # ProductName = serializers.CharField(max_length=200)
    # ProductPrice = serializers.DecimalField(max_digits=10, decimal_places=2)
    # User = serializers.ForeignKey(UserModel, on_delete=models.CASCADE)
    # user = UserModel.objects.get(id=)
    class Meta:
        model = PoductModel
        fields = ['ProductName','ProductPrice','ProductDescription','ProductImage']
        # User = serializers.Field(source='User.username')

class UserModelSerializer(serializers.ModelSerializer):
    # firstname = serializers.CharField(max_length=200)
    class Meta:
        model = UserModel
        fields = ['firstname','username', 'lastname', 'address']

        # def create(self, data):
        #     return UserModel.objects.create_user(
        #     address = data.get("address"),
        #     firstname=data.get("firstname"),
        #     lastname=data.get("lastname"),
        #      = data.get("phone"),
        # )

