from django.urls import path, include
from rest_framework import routers

from shopping_list.api.viewsets import ShoppingItemViewSet
from shopping_list import views


router = routers.DefaultRouter()
router.register("shopping-items", ShoppingItemViewSet, basename="shopping-items")

urlpatterns = [
    path("about/", views.about, name="about"),
    path("api/", include(router.urls)),
]