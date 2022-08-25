from django.urls import path, include
from product.views import ProductViewSet
from product_order.views import ProductOrderViewSet
from supplier.views import SupplierViewSet
from customer.views import CustomerViewSet
from customer_group.views import CustomerGroupViewSet
from category.views import CategoryViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'product', ProductViewSet)
router.register(r'product_order', ProductOrderViewSet)
router.register(r'supplier', SupplierViewSet)
router.register(r'customer', CustomerViewSet)
router.register(r'customer_group', CustomerGroupViewSet)
router.register(r'category', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]