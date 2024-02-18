from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CustomUser

from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.decorators import permission_classes

from .serializers import AccountSerializer

from django.shortcuts import get_object_or_404


# Create your views here.
class createAccount(APIView):
    def get(self,request):
        snippets = CustomUser.objects.all()
        serializer = houseSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.error)

class accountDetail(APIView):
    permission_classes = [IsAuthenticated,IsAdminUser]

    def get(self,request,pk):
        snippets = get_object_or_404(CustomUser,pk=pk)
        serializer = AccountSerializer(snippets)
        return Response(serializer.data)

    def patch(self,request,pk):
        snippets = get_object_or_404(CustomUser,pk=pk)
        serializer = AccountSerializer(snippets,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def put(self,request,pk):
        snippets = get_object_or_404(order,pk=pk)
        serializer = orderSerializer(snippets,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def delete(self,request,pk):
        snippets = get_object_or_404(CustomUser,pk=pk)
        serializer = AccountSerializer(snippets,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.delete()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)