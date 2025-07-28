from django.urls import path
from .views import CategoryListCreate, TransactionListCreate, TransactionDetail

urlpatterns = [
    path('categories/',CategoryListCreate.as_view()),
    path('transactions/',TransactionListCreate.as_view()),
    path('transactions/<int:pk>/',TransactionDetail.as_view()),
]
