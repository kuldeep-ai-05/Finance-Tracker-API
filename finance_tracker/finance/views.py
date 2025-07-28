from rest_framework import generics, permissions
from .models import Category,Transaction
from .serializers import CategorySerializer, TransactionSerializer

class CategoryListCreate(generics.ListCreateAPIView):
    serializer_class=CategorySerializer

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)
    
    def perform_create(self,serializer):
        serializer.save(user=self.request.user)

class TransactionListCreate(generics.ListCreateAPIView):
    serializer_class=TransactionSerializer

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
class TransactionDetail(generics.RetrieveDestroyAPIView):
    serializer_class=TransactionSerializer

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)