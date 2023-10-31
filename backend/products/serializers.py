from rest_framework import serializers

from .models import Product

class PrimaryProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount'
        ]
    
    def get_my_discount(self, obj):
        return obj.get_discount()
    

# class SecondaryProductSerializer(serializers.ModelSerializer):
#     my_discount = serializers.SerializerMethodField(read_only=True)
    
#     class Meta:
#         model = Product
#         fields = [
#             'title',
#             'content',
#             'price',
#             'sale_price',
#             'my_discount'
#         ]
    
#     def get_my_discount(self, obj):
#         return obj.get_discount()