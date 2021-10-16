from django.urls import include, path
from rest_framework import routers


from users.views import UserViewSet


router = routers.DefaultRouter()
router.register(r"users-api", UserViewSet)

app_name = "users"
urlpatterns = [
    path("", include(router.urls,)),
    path("user/create/", UserViewSet.as_view(), name="user-create"),
    #path("uesr/<int:pk>/", CategoryDetail.as_view(), name="user-detail")
]