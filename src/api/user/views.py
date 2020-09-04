from django.http import JsonResponse
from django.db import transaction
from rest_framework.generics import GenericAPIView
from rest_framework.parsers import (
    FormParser,
    MultiPartParser
)
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from user.serializers import UserSerializer
from user.models import User


class UsersView(GenericAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    parser_classes = (FormParser, MultiPartParser)

    @swagger_auto_schema(
        operation_summary='我是 GET 的摘要',
        operation_description='我是 GET 的說明',
        manual_parameters=[
           openapi.Parameter(
               name='email',
               in_=openapi.IN_PATH,
               description='Email',
               type=openapi.TYPE_STRING
           ),

        ]
    )
    def get(self, request, *args, **krgs):
        users = self.get_queryset()
        serializer = self.serializer_class(users, many=True)
        data = serializer.data
        return JsonResponse(data, safe=False)

    @swagger_auto_schema(
        operation_summary='我是 POST 的摘要',
        operation_description='我是 POST 的說明',
        # request_body=openapi.Schema(
        #     type=openapi.TYPE_OBJECT,
        #     properties={
        #         'name': openapi.Schema(
        #             type=openapi.TYPE_STRING,
        #             description='User Name'
        #         )
        #     }
        # )
        manual_parameters=[
           openapi.Parameter(
               name='image',
               in_=openapi.IN_FORM,
               description='Image',
               type=openapi.TYPE_FILE
           ),
       ],
       deprecated=True
    )
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
        return JsonResponse(data)
