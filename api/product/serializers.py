from rest_framework import serializers
from .models import Product

class Productserializers(serializers.HyperlinkedModelSerializer):
    image = serializers.ImageField(max_length=None,allow_null=True,allow_empty_file=False,required=False)
    class Meta:
        model = Product
        fields = ('id','name','descriptions','price','image','category')