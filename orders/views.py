from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

from .serializers import orderSerializer
from .models import order

from django.shortcuts import get_object_or_404
# Create your views here.
class ordersList(APIView):

    def get(self,request):
        snippets = order.objects.all()
        serializer = orderSerializer(snippets, many=True)
        return Response(serializer.data)

    @permission_classes([IsAuthenticated])
    def post(self,request):
        serializer = orderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

class orderDetail(APIView):

    def get(self,request,pk):
        snippets = get_object_or_404(order,pk=pk)
        serializer = orderSerializer(snippets)
        return Response(serializer.data)

    @permission_classes([IsAuthenticated])
    def patch(self,request,pk):
        snippets = get_object_or_404(order,pk=pk)
        serializer = orderSerializer(snippets,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    @permission_classes([IsAuthenticated])
    def put(self,request,pk):
        snippets = get_object_or_404(order,pk=pk)
        serializer = orderSerializer(snippets,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    
    @permission_classes([IsAuthenticated])
    def delete(self,request,pk):
        snippets = get_object_or_404(order,pk=pk)
        serializer = orderSerializer(snippets,data=request.data)
        if serializer.is_valid():
            serializer.delete()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
