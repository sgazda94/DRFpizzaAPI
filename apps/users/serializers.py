from dj_rest_auth.registration.serializers import RegisterSerializer
from django.db import transaction
from rest_framework import serializers


class CustomRegisterSerializer(RegisterSerializer):
    phone_number = serializers.CharField(max_length=9)

    @transaction.atomic
    def save(self, request):
        user = super().save(request)
        user.phone_number = self.data.get("phone_number")
        user.save()
        return user


# class UserSerializer
