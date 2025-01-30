from django.shortcuts import render
from rest_framework import mixins,generics
from .models import Guests,Reservation,Bus
from .serializer import BusSerializer,GusetSerializer,ReservationSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication 
from rest_framework.permissions import IsAuthenticated
# Create your views here.

## guests
class mixins_list(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset=Guests.objects.all()
    serializer_class=GusetSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)
    
class mixins_pk(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset=Guests.objects.all()
    serializer_class=GusetSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]


    def get(self,request,pk):
        return self.retrieve(request)
    def put(self,request,pk):
        return self.update(request)
    def delete(self,request,pk):
        return self.destroy(request)
    
##bus
class mixins_list_bus(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset=Bus.objects.all()
    serializer_class=BusSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)


class mixins_pk_bus(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)
    
@api_view(['GET'])
def searchbus(request):
    bus=Bus.objects.filter(
        destination=request.data['destination']
    )
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    serializer=BusSerializer(bus,many=True)
    return Response(serializer.data)
    
#rservation
class mixins_list_reservation(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset=Reservation.objects.all()
    serializer_class=ReservationSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)
    

@api_view(['GET'])
def detailsreservation(request):
    reservation=Reservation.objects.filter(
        pk=request.data['pk']
    )
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    serializer=ReservationSerializer(reservation,many=True)
    return Response(serializer.data)
      
