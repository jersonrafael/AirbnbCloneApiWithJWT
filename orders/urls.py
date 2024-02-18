from django.urls import path
from .views import orderDetail,ordersList


urlpatterns = [
    path('orders/', ordersList.as_view()),
    path('order/<int:pk>/', orderDetail.as_view()),

]