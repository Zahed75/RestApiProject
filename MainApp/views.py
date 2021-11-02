from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializer import *
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.


@api_view(['GET'])
def home(request):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    stu_obj = Student.objects.all()
    Serializer = StudentSerializer(stu_obj, many=True)

    return Response({'status': 300, 'payload': Serializer.data, 'message': "Data Get"})


@api_view(['POST'])
def post_data(request):
    data = request.data
    Serializer = StudentSerializer(data=request.data)
    # if request.data['age'] <= '18':
    #     return Response({'status':403,'message':"age should be >18"})
    if not Serializer.is_valid():
        print(Serializer.errors)
        return Response({'status': 403, 'errors': Serializer.errors, 'message': "Something Went Wrong"})
    Serializer.save()

    return Response({'status': 200, 'payload': Serializer.data, 'message': 'Data Sent Successfully'})


@api_view(['PATCH'])
def update_student(request, id):
    try:
        stu_obj = Student.objects.get(id=id)
        Serializer = StudentSerializer(stu_obj, data=request.data, partial=True)

        if not Serializer.is_valid():
            return Response({'status': 403, 'errors': Serializer.errors, 'message': 'Something wnent wrong'})

        Serializer.save()

        return Response({'status': 200, 'payload': Serializer.data, 'message': 'data saved'})

    except Exception as e:
        return Response({'status': 403, 'message': 'invalid id'})


# @api_view(['DELETE'])
# def delete_student(request):
#     try:
#         id = request.GET.get('id')
#         stu_obj = Student.objects.get(id=id)
#         stu_obj.delete()
#         return Response({'status': 200, 'message': 'deleted'})
#
#     except Exception as e:
#         print(e)
#         return Response({'status': 403, 'message': 'invalid id'})


@api_view(['DELETE'])
def delete_student(request, id):
    try:
        stu_obj = Student.objects.get(id=id)
        stu_obj.delete()
        return Response({'status': 202, 'mesaage': 'deleted'})

    except Exception as e:
        print(e)
        return Response({'status': 403, 'message': 'invalid'})


@api_view(['GET'])
def get_book(request):
    book_obj = Book.objects.all()
    serializers = BookSerializer(book_obj, many=True)
    return Response({'status': 202, 'payload': serializers.data})


class RegisterUser(APIView):
    def post(self, request):
        serializer=RegisterSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'status':403,'errors':serializer.errors,'message':"something went wrong"})

        serializer.save()

        user = User.objects.get(username=serializer.data['username'])
        token_obj, _ = Token.objects.get_or_create(user=user)

        return Response(
            {'status': 202, 'payload': serializer.data, 'token': str(token_obj), 'message': "your data was saved"})
