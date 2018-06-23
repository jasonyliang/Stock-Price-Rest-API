from django.shortcuts import render
from .serializers import StockSerializers, UserSerializer
from rest_framework import viewsets
from .models import Stocks

import django_filters.rest_framework
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model

# Create your views here.
class StocksViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Stocks.objects.all()
    serializer_class = StockSerializers

    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filter_fields = ('market', )
    ordering = ('-gained_values')
    search_fields = ('stock_name',)


class CreateUser(CreateAPIView):
    model = get_user_model()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer