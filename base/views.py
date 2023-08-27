from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import *
from .models import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from .permissions import FrontDeskUserPermission
from django.contrib.auth.hashers import make_password

# Create your views here.
#----------------------------User------------------------------------

@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        request.data['username'] = 'user'
        password = request.data.get("password")
        hash_password = make_password(password)
        request.data['password'] = hash_password
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('User created!')
        else:
            return Response(serializer.errors)

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = authenticate(username=email,password=password)
    if user != None:
        token,_ = Token.objects.get_or_create(user=user)
        return Response({'token':token.key})
    else: 
        return Response(user)

#----------------------------roomType------------------------------------

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
        

#----------------------------Room------------------------------------
    
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
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, FrontDeskUserPermission]

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
        
#----------------------------Customer------------------------------------
@api_view(['GET','POST'])
def CustomerView(request):
    if request.method == 'GET':
        #get all the objects from the roomtype
        customer_objects = CustomerDetail.objects.all()
        serializer = CustomerDetailSerializer(customer_objects,many=True)#many=True works like for loop
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CustomerDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
@api_view(['GET','PUT','DELETE'])
def CustomerDetailView(request,pk):
    if request.method == 'GET':
        try:
            customer_details_obj = CustomerDetail.objects.get(id=pk)
        except:
            return Response('Data not Found!')
        serializer = CustomerDetailSerializer(customer_details_obj)
        return Response(serializer.data)
    elif request.method == 'PUT':
        try:
            customer_details_obj = CustomerDetail.objects.get(id=pk)
        except:
            return Response('Data not Found!')
        serializer = CustomerDetailSerializer(customer_details_obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    elif request.method == 'DELETE':
        try:
            customer_details_obj = CustomerDetail.objects.get(id=pk)
        except:
            return Response('Data not Found!')
        customer_details_obj.delete()
        return Response('Data Deleted!')   

#----------------------------Bill------------------------------------
@api_view(['GET','POST'])
def BillView(request):
    if request.method == 'GET':
        #get all the objects from the roomtype
        bill_objects = Bill.objects.all()
        serializer = BillSerializer(bill_objects,many=True)#many=True works like for loop
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = BillSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
@api_view(['GET','PUT','DELETE'])
def BillDetailView(request,pk):
    if request.method == 'GET':
        try:
            bill_detail_obj = Bill.objects.get(id=pk)
        except:
            return Response('Data not Found!')
        serializer = BillSerializer(bill_detail_obj)
        return Response(serializer.data)
    elif request.method == 'PUT':
        try:
            bill_detail_obj = Bill.objects.get(id=pk)
        except:
            return Response('Data not Found!')
        serializer = BillSerializer(bill_detail_obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    elif request.method == 'DELETE':
        try:
            bill_detail_obj = Bill.objects.get(id=pk)
        except:
            return Response('Data not Found!')
        bill_detail_obj.delete()
        return Response('Data Deleted!')   

#----------------------------PaymentInfo------------------------------------
@api_view(['GET','POST'])
def PaymentInfoView(request):
    if request.method == 'GET':
        #get all the objects from the roomtype
        payment_objects = PaymentInfo.objects.all()
        serializer = PaymentInfoSerializer(payment_objects,many=True)#many=True works like for loop
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PaymentInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
@api_view(['GET','PUT','DELETE'])
def PaymentInfoDetailView(request,pk):
    if request.method == 'GET':
        try:
            payment_detail_obj = PaymentInfo.objects.get(id=pk)
        except:
            return Response('Data not Found!')
        serializer = PaymentInfoSerializer(payment_detail_obj)
        return Response(serializer.data)
    elif request.method == 'PUT':
        try:
            payment_detail_obj = PaymentInfo.objects.get(id=pk)
        except:
            return Response('Data not Found!')
        serializer = PaymentInfoSerializer(payment_detail_obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    elif request.method == 'DELETE':
        try:
            payment_detail_obj = PaymentInfo.objects.get(id=pk)
        except:
            return Response('Data not Found!')
        payment_detail_obj.delete()
        return Response('Data Deleted!')  
    

#----------------------------EmployeeInfo------------------------------------
@api_view(['GET','POST'])
def EmployeeInfoView(request):
    if request.method == 'GET':
        #get all the objects from the roomtype
        employee_objects = EmployeeInfo.objects.all()
        serializer = EmployeeInfoSerializer(employee_objects,many=True)#many=True works like for loop
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = EmployeeInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
@api_view(['GET','PUT','DELETE'])
def EmployeeInfoDetailView(request,pk):
    if request.method == 'GET':
        try:
            employee_detail_obj = EmployeeInfo.objects.get(id=pk)
        except:
            return Response('Data not Found!')
        serializer = EmployeeInfoSerializer(employee_detail_obj)
        return Response(serializer.data)
    elif request.method == 'PUT':
        try:
            employee_detail_obj = Bill.objects.get(id=pk)
        except:
            return Response('Data not Found!')
        serializer = EmployeeInfoSerializer(employee_detail_obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    elif request.method == 'DELETE':
        try:
            employee_detail_obj = EmployeeInfo.objects.get(id=pk)
        except:
            return Response('Data not Found!')
        employee_detail_obj.delete()
        return Response('Data Deleted!')  
    

#----------------------------MenuType------------------------------------
@api_view(['GET','POST'])
def MenuTypeView(request):
    if request.method == 'GET':
        #get all the objects from the roomtype
        menuType_objects = MenuType.objects.all()
        serializer = MenuTypeSerializer(menuType_objects,many=True)#many=True works like for loop
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MenuTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
@api_view(['GET','PUT','DELETE'])
def MenuTypeDetailView(request,pk):
    if request.method == 'GET':
        try:
            menuType_detail_obj = MenuType.objects.get(id=pk)
        except:
            return Response('Data not Found!')
        serializer = MenuTypeSerializer(menuType_detail_obj)
        return Response(serializer.data)
    elif request.method == 'PUT':
        try:
            menuType_detail_obj = MenuType.objects.get(id=pk)
        except:
            return Response('Data not Found!')
        serializer = MenuTypeSerializer(menuType_detail_obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    elif request.method == 'DELETE':
        try:
            menuType_detail_obj = MenuType.objects.get(id=pk)
        except:
            return Response('Data not Found!')
        menuType_detail_obj.delete()
        return Response('Data Deleted!')  
    

#----------------------------Food------------------------------------
@api_view(['GET','POST'])
def FoodView(request):
    if request.method == 'GET':
        #get all the objects from the roomtype
        food_objects = Food.objects.all()
        serializer = FoodSerializer(food_objects,many=True)#many=True works like for loop
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = FoodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
@api_view(['GET','PUT','DELETE'])
def FoodDetailView(request,pk):
    if request.method == 'GET':
        try:
            food_detail_obj = Food.objects.get(id=pk)
        except:
            return Response('Data not Found!')
        serializer = FoodSerializer(food_detail_obj)
        return Response(serializer.data)
    elif request.method == 'PUT':
        try:
            food_detail_obj = Food.objects.get(id=pk)
        except:
            return Response('Data not Found!')
        serializer = FoodSerializer(food_detail_obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    elif request.method == 'DELETE':
        try:
            food_detail_obj = Food.objects.get(id=pk)
        except:
            return Response('Data not Found!')
        food_detail_obj.delete()
        return Response('Data Deleted!')  
    

#----------------------------Service------------------------------------
@api_view(['GET','POST'])
def ServiceView(request):
    if request.method == 'GET':
        #get all the objects from the roomtype
        service_objects = Service.objects.all()
        serializer = ServiceSerializer(service_objects,many=True)#many=True works like for loop
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
@api_view(['GET','PUT','DELETE'])
def ServiceDetailView(request,pk):
    if request.method == 'GET':
        try:
            service_detail_obj = Service.objects.get(id=pk)
        except:
            return Response('Data not Found!')
        serializer = ServiceSerializer(service_detail_obj)
        return Response(serializer.data)
    elif request.method == 'PUT':
        try:
            bill_detail_obj = Service.objects.get(id=pk)
        except:
            return Response('Data not Found!')
        serializer = ServiceSerializer(service_detail_obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    elif request.method == 'DELETE':
        try:
            service_detail_obj = Service.objects.get(id=pk)
        except:
            return Response('Data not Found!')
        service_detail_obj.delete()
        return Response('Data Deleted!')  
    

#----------------------------Facilities------------------------------------
@api_view(['GET','POST'])
def FacilitiesView(request):
    if request.method == 'GET':
        #get all the objects from the roomtype
        facilities_objects = Facilities.objects.all()
        serializer = FacilitiesSerializer(facilities_objects,many=True)#many=True works like for loop
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = FacilitiesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
@api_view(['GET','PUT','DELETE'])
def FacilitiesDetailView(request,pk):
    if request.method == 'GET':
        try:
            facilities_detail_obj = Bill.objects.get(id=pk)
        except:
            return Response('Data not Found!')
        serializer = FacilitiesSerializer(facilities_detail_obj)
        return Response(serializer.data)
    elif request.method == 'PUT':
        try:
            facilities_detail_obj = Facilities.objects.get(id=pk)
        except:
            return Response('Data not Found!')
        serializer = FacilitiesSerializer(facilities_detail_obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    elif request.method == 'DELETE':
        try:
            facilities_detail_obj = Facilities.objects.get(id=pk)
        except:
            return Response('Data not Found!')
        facilities_detail_obj.delete()
        return Response('Data Deleted!')  



    