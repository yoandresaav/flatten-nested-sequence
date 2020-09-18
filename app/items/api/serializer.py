

from rest_framework import serializers

from ..models import Item

class ItemSerializer(serializers.Serializer):
    """Serializer an items"""
    items = serializers.JSONField()


class ItemModelSerializer(serializers.ModelSerializer):
    """Serializer an item model"""
    class Meta:
        model = Item
        fields = ('result',)
