from rest_framework import generics
from . import serializers
from . import models
from rest_framework.permissions import IsAuthenticated
from . import permissions
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


class CarListCreateView(generics.ListCreateAPIView):
    """Создание и получение списка автомобилей"""
    queryset = models.Car.objects.filter(is_active=True)
    serializer_class = serializers.CarSerializer


class CarRetrieveView(generics.RetrieveAPIView):
    """Получение объекта"""
    queryset = models.Car.objects.filter(is_active=True)
    serializer_class = serializers.CarSerializer


class CarUpdateView(generics.UpdateAPIView):
    """Обновление объекта"""
    permission_classes = (
        IsAuthenticated,
        permissions.CarOwnerPermission
    )
    queryset = models.Car.objects.filter(is_active=True)
    serializer_class = serializers.CarSerializer


class CarDeleteView(generics.DestroyAPIView):
    """Удаление объекта"""
    permission_classes = (
        IsAuthenticated,
        permissions.CarOwnerPermission
    )
    serializer_class = serializers.CarSerializer

    def delete(self, request, *args, pk=None, **kwargs):
        car = get_object_or_404(models.Car,
                                car_id=pk,
                                is_active=True)
        self.check_object_permissions(request, car)
        car.is_active = False
        car.save()
        return Response(
            {
                'message': 'ok',

            },
            status=status.HTTP_204_NO_CONTENT
        )

    # Или

    # def delete(self, request, *args, pk=None, **kwargs):
    #     try:
    #         car = models.Car.objects.get(car_id=pk,
    #                                      is_active=True)
    #         self.check_object_permissions(request, car)
    #         car.is_active = False
    #         car.save()
    #         return Response(
    #             {
    #                 'message': 'ok',
    #
    #             },
    #             status=status.HTTP_204_NO_CONTENT
    #         )
    #     except models.Car.DoesNotExist:
    #         return Response(
    #             {
    #                 'message': 'not_found'
    #             },
    #             status=status.HTTP_404_NOT_FOUND
    #         )

