from django.urls import path
from .views import CartItemView

urlpatterns=[
    path('cart-items/', CartItemView.as_view()),
    path('cart-items/<int:id>', CartItemView.as_view())
]