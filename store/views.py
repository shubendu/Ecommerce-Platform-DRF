from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from rest_framework import status

@api_view()
def product_list(request):
    queryset = Product.objects.select_related('collection').all()
    serializer = ProductSerializer(queryset, many = True, context = {'request':request})
    return Response(serializer.data)

@api_view()
def product_detail(request,id):
    product = get_object_or_404(Product, pk= id)        
    serialzer = ProductSerializer(product)
    return Response(serialzer.data)

@api_view()
def collection_detail(request,pk):
    return Response(pk)