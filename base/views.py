from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import GenericAPIView

# Create your views here.
@api_view(['GET','POST'])
def roomTypeView(request):
    if request.method == 'GET':
        #get all the objects from the roomtype
        room_type_objects = RoomType.objects.all()
        serializer = RoomTypeSerializer(room_type_objects,many=True)#many=True works like for loop
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = RoomTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


@api_view(['GET','PUT','DELETE'])
def roomTypeDetailView(request,pk):
    if request.method == 'GET':
        try:
            room_type_obj = RoomType.objects.get(id=pk)
        except:
            return Response('Data not Found!')
        serializer = RoomTypeSerializer(room_type_obj)
        return Response(serializer.data)
    elif request.method == 'PUT':
        try:
            room_type_obj = RoomType.objects.get(id=pk)
        except:
            return Response('Data not Found!')
        serializer = RoomTypeSerializer(room_type_obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    elif request.method == 'DELETE':
        try:
            room_type_obj = RoomType.objects.get(id=pk)
        except:
            return Response('Data not Found!')
        room_type_obj.delete()
        return Response('Data Deleted!')
        
@api_view(['GET','POST'])
def roomView(request,pk):
    if request.method == 'GET':
        #get all the objects from the roomtype
        room_objects = Room.objects.filter(room_type=pk)
        serializer = RoomSerializer(room_objects,many=True)#many=True works like for loop
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

#class based view
#every method is related
#callable
#generic Api View helps customize
class RoomApiView(GenericAPIView):#genericapiview every http method function is made
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['room_type','status']
    serializer_class = RoomSerializer

    def get(self,request):
        room_objects = Room.objects.all()
        filter_objects = self.filter_queryset(room_objects)
        serializer = self.serializer_class(filter_objects,many=True)#many=True works like for loop
        return Response(serializer.data)
    
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
