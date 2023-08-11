import pandas as pd
from django.core.cache import cache
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import HttpResponse
from rest_framework import generics, permissions
from rest_framework.views import APIView

from products.models import Product
from products.serializers import ProductSerializer


class ProductListAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        queryset = cache.get('product_list_cache')
        if queryset is None:
            queryset = Product.objects.select_related('category')
            cache.set('product_list_cache', queryset)
        return queryset


class ProductCreateAPIView(generics.CreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save()


class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_update(self, serializer):
        serializer.save()


class ProductExcelExport(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        data = []

        for product in products:
            data.append({
                "Name": product.name,
                "Description": product.description,
                "Price": product.price,
                "Category": product.category.name
            })

        df = pd.DataFrame(data)
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="products.xlsx"'
        df.to_excel(response, index=False, engine='openpyxl')

        return response


@receiver(post_save, sender=Product)
def invalidate_product_cache(sender, instance, **kwargs):
    cache.delete('product_list_cache')
