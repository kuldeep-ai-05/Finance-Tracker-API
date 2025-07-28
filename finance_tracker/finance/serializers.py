from rest_framework import serializers
from .models import Category,Transaction

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['id','name']

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Transaction
        fields=['id','category','amount','date','type','description']