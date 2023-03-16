from django.shortcuts import render
from rest_framework import generics
from .models import MenuItem, Category
from .serializers import MenuItemSerializer, CategorySerializer



class CategoriesView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

    #To add the ordering in the API
    ordering_fields = ['price','inventory' ]

    #To add the filter data
    filter_fields = ['price','inventory' ]

    #To implement the search
    search_fields = [ 'category' ]


