from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from . import views

router = routers.DefaultRouter()
router.register(r"", views.BookingViewSet)

urlpatterns = [
    path("menu/", views.MenuItemView.as_view(), name="menu-item"),
    path("menu/<int:pk>", views.SingleMenuItem.as_view(), name="single-menu-item"),
    path("booking/", include(router.urls)),
    path("message/", views.msg),
    path("api-token-auth/", obtain_auth_token, name="api_token_auth"),
]
