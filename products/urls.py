from django.urls import path
from .views import (
    ProductListAPIView, ProductExcelExport,
    ProductCreateAPIView, ProductUpdateAPIView
)

urlpatterns = [
    path('list/', ProductListAPIView.as_view()),
    path('export/excel/', ProductExcelExport.as_view()),
    path('create/', ProductCreateAPIView.as_view()),
    path('update/', ProductUpdateAPIView.as_view())
]
