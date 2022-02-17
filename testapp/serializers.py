from .models import Category, OrderItem
from rest_framework import serializers

# WE NEED TO IMPORT SERIALIZERS FROM REST_FRAMEWORK
#########################################
######## ORDER ITEM SERIALIZERS #########
#########################################

class OrderItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrderItem
        fields='__all__'

#########################################
######## CATEGORY SERIALIZERS #########
#########################################

class CategorysSerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'