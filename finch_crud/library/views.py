from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CarSerializer
from .models import Car

class CarView(APIView):
    def get(self, request):
        cars = Car.objects.all()
        data = CarSerializer(cars, many=True).data
        return Response(data)

    def post(self, request):
        print(request.data)
        car = CarSerializer(data=request.data)
        if car.is_valid():
            car.save()
            return Response(car.data, status=status.HTTP_201_CREATED)
        else:
            return Response(car.errors, status=status.HTTP_400_BAD_REQUEST)

class CarDetailView(APIView):
    def get(self, respect, pk):
        car = get_object_or_404(Car, pk=pk)
        data =  CarSerializer(car).data
        return Response(data)

    def delete(self, request, pk):
        car = get_object_or_404(Car, pk=pk)
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk):
        car = get_object_or_404(Car, pk=pk)
        updated_car = CarSerializer(car, data=request.data)
        if updated_car.is_valid():
            updated_car.save()
            return Response(updated_car.data)
        return Response(updated_car.errors, status=status.HTTP_400_BAD_REQUEST)


    




