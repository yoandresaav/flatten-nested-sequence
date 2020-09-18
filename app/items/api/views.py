from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView

from django.shortcuts import render

from .serializer import ItemSerializer, ItemModelSerializer
from ..models import Item
from ..utils import convert_nested_list_in_flattens_list

class ItemView(APIView):
    """
    Recive nested list and return flatten list.
    """
    def post(self, request, format=None):
        serializer = ItemSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        nested_list = serializer.validated_data['items']
        flatten_list = convert_nested_list_in_flattens_list(nested_list)

        # Save Result flatten list
        Item.objects.create(result=flatten_list)

        return Response({'result': flatten_list})

class ListItem(ListAPIView):
    """List all results"""
    model = Item
    serializer_class = ItemModelSerializer
    queryset = Item.objects.all()
