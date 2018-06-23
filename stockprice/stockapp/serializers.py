from .models import Stocks
from rest_framework import serializers

class StockSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stocks
        fields = ('market', 'stock_name', 'gained_values', 'date_created')
