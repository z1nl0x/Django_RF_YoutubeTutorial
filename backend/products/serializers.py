from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Product
from .validators import validate_title, validate_title_no_hello, unique_product_title

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name="product-detail", lookup_field="pk")
    # email = serializers.EmailField(write_only=True)

    title = serializers.CharField(validators=[validate_title_no_hello, unique_product_title])
    # name = serializers.CharField(source="title", read_only=True)

    class Meta:
        model = Product
        fields = [
            # 'user',
            'url',
            'edit_url',
            # 'email',
            # 'name',
            'pk',
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount',
        ]

    # def validate_title(self, value):
    #     request = self.context.get('request')
    #     user = request.user
    #     qs = Product.objects.filter(user=user, title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} is already a product name.")
    #     return value

    # def create(self, validated_data):
    #     # email = validated_data.pop("email")
    #     obj = super().create(validated_data)
    #     return obj
    
    # def update(self, instance, validated_data):
    #     email = validated_data.pop("email")
    #     # instance.title = validated_data.get('title')
    #     return super().update(instance, validated_data)

    def get_edit_url(self, obj):
        # return f"/api/products/{obj.id}"
        request = self.context.get("request")
        if request is None:
            return None
        return reverse("product-edit", kwargs={"pk": obj.id}, request=request)
    
    def get_my_discount(self, obj):
        # try:
        #     return obj.get_discount()
        # except:
        #     return None

        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        
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