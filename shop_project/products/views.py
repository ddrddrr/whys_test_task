from rest_framework import generics
from .models import Product, ProductImage, ProductAttributes


class ProductListView(generics.ListAPIView):
	model = Product
