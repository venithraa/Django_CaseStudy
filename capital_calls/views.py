from rest_framework import viewsets
from .models import Investor, Bill, CapitalCall
from .serializers import InvestorSerializer, BillSerializer, CapitalCallSerializer
from django.shortcuts import render

def capital_call_management(request):
    return render(request, 'index.html')

class InvestorViewSet(viewsets.ModelViewSet):
    queryset = Investor.objects.all()
    serializer_class = InvestorSerializer

class BillViewSet(viewsets.ModelViewSet):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer

class CapitalCallViewSet(viewsets.ModelViewSet):
    queryset = CapitalCall.objects.all()
    serializer_class = CapitalCallSerializer