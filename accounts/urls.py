from django.urls import path
from .views import createAccount,accountDetail


urlpatterns = [
    path('accounts/', createAccount.as_view()),
    path('account/<int:pk>/', accountDetail.as_view()),
]