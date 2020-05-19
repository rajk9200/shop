from django.shortcuts import render

# Create your views here.

from accounts.models import Profile

from product.models  import Product


from rest_framework import serializers,viewsets

class ProfileSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        # fields =['id','name','mobile']
        fields ="__all__"


class ProfileVie(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerilizer



class ProductSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields =['name','cat','price']
        # fields ="__all__"


class ProductVie(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerilizer







