from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

from django.shortcuts import get_object_or_404


from .serializers import houseSerializer
from .models import house
# Create your views here.
class housesList(APIView):

    def get(self,request):
        snippets = house.objects.all()
        serializer = houseSerializer(snippets, many=True)
        return Response(serializer.data)

class houseDetail(APIView):
    def get(self,request,pk):
        snippet = get_object_or_404(house,pk=pk)
        serializer = houseSerializer(snippet)
        return Response(serializer.data)

    @permission_classes([IsAuthenticated])
    def patch(self,request,pk):
        snippets = get_object_or_404(house,pk=pk)
        serializer = houseSerializer(snippets,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    
    @permission_classes([IsAuthenticated])
    def put(self,request,pk):
        snippets = get_object_or_404(house,pk=pk)
        serializer = houseSerializer(snippets,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    
    @permission_classes([IsAuthenticated])
    def delete(self,request,pk):
        snippets = get_object_or_404(order,pk=pk)
        serializer = houseSerializer(snippets,data=request.data)
        if serializer.is_valid():
            serializer.delete()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)