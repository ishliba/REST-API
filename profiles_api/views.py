from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import status  #to return status codes for API


from profiles_api import serializers
class HelloAPiView(APIView):
    """Test API View"""

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

