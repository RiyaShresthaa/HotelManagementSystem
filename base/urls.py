from django.urls import path
from .views import *


urlpatterns = [
    path('login/',login,name='login'),
    path('register/',register,name='register'),
    path('room_type/',roomTypeView,name='roomType'),
    path('room_type/<pk>',roomTypeDetailView,name='roomTypeDetail'),
    path('room/',RoomApiView.as_view(),name='room'),
    path('customer/',CustomerView,name='customer'),
    path('customer/<pk>',CustomerDetailView,name='customerDetail'),
    path('bill/',BillView,name='bill'),
    path('bill/<pk>',BillDetailView,name='billDetail'),
    path('payment/',PaymentInfoView,name='payment'),
    path('payment/<pk>',PaymentInfoDetailView,name='paymentDetail'),
    path('employee/',EmployeeInfoView,name='employee'),
    path('employee/<pk>',EmployeeInfoDetailView,name='employeeDetail'),
    path('menuType/',MenuTypeView,name='menuType'),
    path('menuType/<pk>',MenuTypeDetailView,name='menuTypeDetail'),
    path('food/',FoodView,name='food'),
    path('food/<pk>',FoodDetailView,name='foodDetail'),
    path('service/',ServiceView,name='service'),
    path('service/<pk>',ServiceDetailView,name='serviceDetail'),
    path('facilities/',FacilitiesView,name='facilities'),
    path('facilities/<pk>',FacilitiesDetailView,name='facilitiesDetail'),
]