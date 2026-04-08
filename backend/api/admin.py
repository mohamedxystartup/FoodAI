from django.contrib import admin    
from .models import CustomUser, Restaurant, Plat, Commande, CommandePlat, Livraison, IARecommandation, IAConversation
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Restaurant)
admin.site.register(Plat)
admin.site.register(Commande)
admin.site.register(CommandePlat)
admin.site.register(Livraison)
admin.site.register(IARecommandation)
admin.site.register(IAConversation)

