from rest_framework.views import APIView
from rest_framework.views import Response


class HelloAPiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of APIview features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete',
            'Is similar to a traditional Django view',
            'Gives you the most control over your application logic',
            'Is maped manually to URLs'

        ]

        return Response({'message' : 'Hello' , 'an_apiview': an_apiview})
