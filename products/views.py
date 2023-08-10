from rest_framework import generics, permissions

from products.models import Product
from products.serializers import ProductSerializer


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.select_related('category')
    serializer_class = ProductSerializer
    permission_classes = (permissions.AllowAny,)
