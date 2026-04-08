from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import  RestaurantViewSet, PlatViewSet, CommandeViewSet, CommandePlatViewSet, LivraisonViewSet, IARecommandationViewSet, IAConversationViewSet

router = DefaultRouter()
router.register("restaurants", RestaurantViewSet)
router.register("plats", PlatViewSet)
router.register("commandes", CommandeViewSet)
router.register("commande-plats", CommandePlatViewSet)
router.register("livraisons", LivraisonViewSet)
router.register("ia-recommandations", IARecommandationViewSet)
router.register("ia-conversations", IAConversationViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
