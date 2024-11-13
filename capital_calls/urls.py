from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InvestorViewSet, BillViewSet, CapitalCallViewSet
from . import views

router = DefaultRouter()
router.register(r'investors', InvestorViewSet)
router.register(r'bills', BillViewSet)
router.register(r'capital_calls', CapitalCallViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.capital_call_management, name='capital_call_management'),
]