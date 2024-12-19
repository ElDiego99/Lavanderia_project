from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Cliente, Servicio, Orden 
from .serializers import ClienteSerializer, ServicioSerializer, OrdenSerializer

# Clase base para reducir código repetido
class BaseList(APIView):
    model = None
    serializer_class = None

    def get(self, request):
        objetos = self.model.objects.all()
        serializer = self.serializer_class(objetos, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BaseDetail(APIView):
    model = None
    serializer_class = None

    def get_object(self, pk):
        return get_object_or_404(self.model, pk=pk)

    def get(self, request, pk):
        objeto = self.get_object(pk)
        serializer = self.serializer_class(objeto)
        return Response(serializer.data)

    def put(self, request, pk):
        objeto = self.get_object(pk)
        serializer = self.serializer_class(objeto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        objeto = self.get_object(pk)
        objeto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Implementaciones específicas
class ClienteList(BaseList):
    model = Cliente
    serializer_class = ClienteSerializer

class ClienteDetail(BaseDetail):
    model = Cliente
    serializer_class = ClienteSerializer

class ServicioList(BaseList):
    model = Servicio
    serializer_class = ServicioSerializer

class ServicioDetail(BaseDetail):
    model = Servicio
    serializer_class = ServicioSerializer

class OrdenList(BaseList):
    model = Orden
    serializer_class = OrdenSerializer

class OrdenDetail(BaseDetail):
    model = Orden
    serializer_class = OrdenSerializer