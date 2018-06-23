from .models import Stocks
from rest_framework import serializers
from django.contrib.auth import get_user_model


class StockSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stocks
        fields = ('market', 'stock_name', 'gained_values', 'date_created')


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)

    def create(self, validated_data):
        user = get_user_model().objects.create(
            username= validated_data['username']

        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ('username', 'password')
