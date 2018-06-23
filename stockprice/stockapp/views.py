from django.shortcuts import render
from .serializers import StockSerializers
from rest_framework import viewsets
from .models import Stocks

# Create your views here.
class StocksViewSet(viewsets.ModelViewSet):
    queryset = Stocks.objects.all().order_by('-date_joined')
    serializer_class = StockSerializers

