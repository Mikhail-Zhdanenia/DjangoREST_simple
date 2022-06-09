from rest_framework import generics
from cars.serializers import CarDetailSerializer, CarListSerializer
from cars.models import Car
from cars.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication

class CarCreateView(generics.CreateAPIView): #add from web interface our models in BD
    serializer_class = CarDetailSerializer


class CarsListView(generics.ListAPIView):
    serializer_class = CarListSerializer
    queryset = Car.objects.all()    #get all data from model car
    permission_classes = (IsAdminUser, )


class CarsDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarDetailSerializer
    queryset = Car.objects.all()
    permission_classes = (IsOwnerOrReadOnly, ) #get all data from model car