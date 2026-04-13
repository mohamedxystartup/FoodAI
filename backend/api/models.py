from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
# Create your models here.


class CustomUserManager(BaseUserManager):
    def create_user(self, email, nom, mot_de_passe=None, **extra_fields):
        if not email:
            raise ValueError("L'email est obligatoire")
        email = self.normalize_email(email)
        user = self.model(email=email, nom=nom, **extra_fields)
        user.set_password(mot_de_passe)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nom, mot_de_passe=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, nom, mot_de_passe, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = [
        ("client", "Client"),
        ("restaurant", "Restaurant"),
        ("livreur", "Livreur"),
        ("admin", "Admin"),
    ]
    nom = models.CharField(max_length=255)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default="client")

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["nom"]

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
class Restaurant(models.Model):
    nom = models.CharField(max_length=255)
    localisation = models.CharField(max_length=255, blank=True, null=True)
    note = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="restaurants")

    def __str__(self):
        return self.nom

class Plat(models.Model):
    nom = models.CharField(max_length=255)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    categorie = models.CharField(max_length=100, blank=True, null=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="plats")

    def __str__(self):
        return f"{self.nom} - {self.restaurant.nom}"

class Commande(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="commandes")
    statut = models.CharField(max_length=50, choices=[("pending","En attente"),("confirmed","Confirmée"),("delivered","Livrée")])
    total = models.DecimalField(max_digits=10, decimal_places=2)
    adresse = models.CharField(max_length=255)

    def __str__(self):
        return f"Commande {self.id} - {self.user.nom}"

class CommandePlat(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE, related_name="commande_plats")
    plat = models.ForeignKey(Plat, on_delete=models.CASCADE)
    quantite = models.IntegerField(default=1)

class Livraison(models.Model):
    commande = models.OneToOneField(Commande, on_delete=models.CASCADE)
    livreur = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, limit_choices_to={"role":"livreur"})
    statut = models.CharField(max_length=50)

class IARecommandation(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    preferences = models.TextField(blank=True, null=True)
    historique = models.TextField(blank=True, null=True)

class IAConversation(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    message_user = models.TextField()
    message_ia = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

