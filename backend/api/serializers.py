from rest_framework import serializers
from .models import CustomUser, Restaurant, Plat, Commande, CommandePlat, Livraison, IARecommandation, IAConversation

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id","nom","telephone","email","role"]

class UserRegistrationSerializer(serializers.ModelSerializer):
    mot_de_passe = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = CustomUser
        fields = ["nom", "telephone", "email", "role", "mot_de_passe"]

    def create(self, validated_data):
        mot_de_passe = validated_data.pop('mot_de_passe')
        user = CustomUser(**validated_data)
        user.set_password(mot_de_passe)
        user.save()
        return user

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = "__all__"

class PlatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plat
        fields = "__all__"

class CommandePlatSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommandePlat
        fields = "__all__"

class CommandeSerializer(serializers.ModelSerializer):
    commande_plats = CommandePlatSerializer(many=True, read_only=True)
    class Meta:
        model = Commande
        fields = "__all__"

class LivraisonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livraison
        fields = "__all__"

class IARecommandationSerializer(serializers.ModelSerializer):
    class Meta:
        model = IARecommandation
        fields = "__all__"

class IAConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = IAConversation
        fields = "__all__"
