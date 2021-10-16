from rest_framework.decorators import action
from users.serializers import UserSerializer
from rest_framework import viewsets, permissions
from rest_framework.response import Response

from django.contrib.auth.models import User
from app.errors import ObjectAlreadyExists, ValidationError
from users.utils import UserErrorMessages
from users.services import UserToolKit


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create_user(self, request):
        data = request.POST or request.data

        try:
            email = data["email"]
            password = data["password"]
        except KeyError:
            return   Response({"error": UserErrorMessages.REQUEST_FIELDS_ERROR.value}, status=400)

        try:
            user = UserToolKit.create_user(
                email=email,
                password=password
            )
        except ValidationError as exc:
            return Response({"error": str(exc)}, status=400)
        except ObjectAlreadyExists:
            return Response({"error": UserErrorMessages.NON_UNIQUE_EMAIL_ERROR.value}, status=400)

        serializer = UserSerializer(instance=user)
        return Response(serializer.data, status=201)

class create:
    pass

    