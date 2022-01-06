from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from ..models.toy import Toy
from ..serializers import ToySerializer, ToyReadSerializer

class ToysView(APIView):
    def get(self,request):
        print(request)
        toys = Toy.objects.all()
        data = ToyReadSerializer(toys, many=True).data
        return Response(data)

    serializer_class = ToySerializer
    def post(self, request):
        print(request.data)
        toy = ToySerializer(data=request.data)
        if toy.is_valid():
            t = toy.save()
            return Response(toy.data, status=status.HTTP_201_CREATED)
        else:
            return Response(toy.errors, status=status.HTTP_400_BAD_REQUEST)

class ToyDetail(APIView):
    def get(self, request, pk):
        toy = get_object_or_404(Toy, pk=pk)
        data = ToyReadSerializer(toy).data
        return Response(data)

    def patch(self, request, pk):
        toy - get_object_or_404(Toy, pk=pk)
        ts = ToySerializer(toy, data=request.data, partial=True)
        if ts.is_valid():
            ts.save()
            return Response(ts.data)
            return Response(ts.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        toy = get_object_or_404(Toy, pk=pk)
        toy.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


