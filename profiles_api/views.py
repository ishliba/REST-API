from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import status  #to return status codes for API
from rest_framework import viewsets

from django.shortcuts import render
file = "/test.html"

from profiles_api import serializers

def test(request):
    hi = "My name is manish"
    return render(request, 'test.html')


class HelloAPiView(APIView):
    """Test API View - HTTP method"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIview features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete',
            'Is similar to a traditional Django view',
            'Gives you the most control over your application logic',
            'Is maped manually to URLs'

        ]

        return Response({'message' : 'Hello' , 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with your name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"Hello {name}"

            return Response({'message': message})

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})


    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'method': 'PATCH'})



    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})



class HelloViewSet(viewsets.ViewSet):
    """Test APi viewset"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello method"""
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLS using Routers',
            'Provides more functionality with less code',
        ]
        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': {message}})

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self,request,pk=None):
        """Handle getting an object by its D"""
        return Response({'http_method':'GET'})

    def update(self,request,pk=None):
        """Handle updating an object"""
        return Response({'http_method':'PUT'})

    def partial_update(self,request,pk=None):
        """Handle updating part of an object"""
        return Response({'http_method': 'PATCH'})

    def destroy(self,request,pk=None):
        """Handle removing an object"""
        return Response({'http_method': 'DELETE'})


