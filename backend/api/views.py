from django.shortcuts import render
from django.http import JsonResponse
import json
from products.models import Product
from django.forms.models import model_to_dict


#DRF Importings

from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.serializers import PrimaryProductSerializer

# @api_view(["GET", "POST"])
# def api_home(request, *args, **kwargs):

#     # print(request.GET) # url query params


#     # body = request.body # Byte string of JSON data
#     # data = {}

#     # try:
#     #     data = json.loads(body)
#     # except:
#     #     pass


#     # print(data.keys())
#     # data['headers'] = dict( request.headers) # header converted to a python dictionary
#     # data['content-type'] = request.content_type
#     # data['params'] = dict(request.GET)
#     # print(data)

#     model_data = Product.objects.all().order_by("?").first()
#     data = {}
    
#     if model_data:
#         # data['id'] = model_data.id
#         # data['title'] = model_data.title
#         # data['content'] = model_data.content1
#         # data['price'] = model_data.price

#         data = model_to_dict(model_data, fields=['title', 'price'])

#     return JsonResponse(data)








# @api_view(["GET", "POST"])
# def api_home(request, *args, **kwargs):

#     if request.method != "POST":
#         return Response({"detail": "GET not allowed"}, status=405)

#     model_data = Product.objects.all().order_by("?").first()
#     data = {}
    
#     if model_data:
        
#         data = model_to_dict(model_data, fields=['title', 'price'])

#     return JsonResponse(data)


# @api_view(["GET"])
# def api_home(request, *args, **kwargs):

#     # if request.method != "POST":
#     #     return Response({"detail": "GET not allowed"}, status=405)

#     model_data = Product.objects.all().order_by("?").first()
#     data = {}
    
#     if model_data:
        
#         data = model_to_dict(model_data, fields=['id','title', 'price', 'sale_price'])

#     return JsonResponse(data)







# BEGINNING WITH SERIALIZERS

@api_view(["GET"])
def api_home(request, *args, **kwargs):

    instance = Product.objects.all().order_by("?").first()
    data = {}
    
    if instance:
        
        # data = model_to_dict(model_data, fields=['id','title', 'price', 'sale_price'])

        data = PrimaryProductSerializer(instance).data

    return JsonResponse(data)