from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer class convert all records into json format.
    """
    class Meta:
        model = Product
        fields = '__all__'