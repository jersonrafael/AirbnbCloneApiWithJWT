from django.urls import path
from .views import housesList,houseDetail


urlpatterns = [
    path('houses/', housesList.as_view()),
    path('house/<int:pk>/', houseDetail.as_view()),
]