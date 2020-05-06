from django.shortcuts import render
from django.http import JsonResponse
from django.db import transaction
from rest_framework.generics import GenericAPIView

from user.serializers import UserSerializer 
from django.contrib.auth.models import User


class UsersView(GenericAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **krgs):
        users = self.get_queryset()
        serializer = self.serializer_class(users, many=True)
        data = serializer.data
        return JsonResponse(data, safe=False)

    def post(self, request, *args, **krgs):
        data = request.data
        try:
            serializer = self.serializer_class(data=data)
            serializer.is_valid(raise_exception=True)
            with transaction.atomic():
                serializer.save()
            data = serializer.data
        except Exception as e:
            data = {'error': str(e)}
        return JsonResponse(data, safe=False)
