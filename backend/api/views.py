from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics, status
from rest_framework import viewsets
from .models import CustomUser, Restaurant, Plat, Commande, CommandePlat, Livraison, IARecommandation, IAConversation
from .serializers import UserSerializer, UserRegistrationSerializer, RestaurantSerializer, PlatSerializer, CommandeSerializer, CommandePlatSerializer, LivraisonSerializer, IARecommandationSerializer, IAConversationSerializer
# Create your views here.


class CreateUserView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class PlatViewSet(viewsets.ModelViewSet):
    queryset = Plat.objects.all()
    serializer_class = PlatSerializer

class CommandeViewSet(viewsets.ModelViewSet):
    queryset = Commande.objects.all()
    serializer_class = CommandeSerializer

class CommandePlatViewSet(viewsets.ModelViewSet):
    queryset = CommandePlat.objects.all()
    serializer_class = CommandePlatSerializer

class LivraisonViewSet(viewsets.ModelViewSet):
    queryset = Livraison.objects.all()
    serializer_class = LivraisonSerializer

class IARecommandationViewSet(viewsets.ModelViewSet):
    queryset = IARecommandation.objects.all()
    serializer_class = IARecommandationSerializer

class IAConversationViewSet(viewsets.ModelViewSet):
    queryset = IAConversation.objects.all()
    serializer_class = IAConversationSerializer
