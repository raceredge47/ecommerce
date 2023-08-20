from rest_framework import viewsets
from .serializers import ProductSerializer                           # import product serializer from serializer.py file.
from .models import Product                                          # import product model from models.py file.
from rest_framework.authentication import SessionAuthentication      # import session authentication.
from rest_framework.permissions import IsAuthenticatedOrReadOnly     # import permissions.

class ProductViewSet(viewsets.ModelViewSet):
    """
    API view to retrieve list of posts or create new.
    View class perform all CRUD operation and also perform both operations complete/partially update.
    """
    queryset = Product.objects.all()          #geting all objects from database.
    serializer_class = ProductSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]


