from rest_framework import generics, status
from rest_framework.response import Response

from . import serializers
from .models import Order


class HelloOrderView(generics.GenericAPIView):
    def get(self, request):
        return Response(data={"message": "Hello Auth"}, status=status.HTTP_200_OK)


class OrderCreateListView(generics.GenericAPIView):
    serializer_class = serializers.OrderCreationSerializer
    queryset = Order.objects.all()

    def get(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def past(self, request):
        pass


class OrderDetailsView(generics.GenericAPIView):
    def get(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass
