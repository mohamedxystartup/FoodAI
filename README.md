# 🍽️ FOOD AI - MVP

## 📌 Introduction

Food AI est une plateforme de commande de nourriture en ligne adaptée au marché africain. L'objectif est de lancer rapidement un MVP simple, efficace et sécurisé, avec une IA de recommandation basée sur le budget et les préférences des utilisateurs.

---

## 🚀 Fonctionnalités Principales

### 👤 Côté Utilisateur
- Inscription (téléphone recommandé, OTP SMS optionnel)
- Connexion
- Voir restaurants
- Voir menus
- Passer commande
- Suivi du statut de commande

### 🏪 Côté Restaurant
- Création de compte restaurant
- Ajout de menus
- Réception des commandes
- Statut commande (accepté / refusé)
- Validation manuelle par admin (photos, GPS, téléphone)

### 🚚 Côté Livreur (Phase 2)
- Non obligatoire pour le MVP initial

### 👨‍💼 Côté Admin
- Validation des restaurants
- Gestion des utilisateurs et restaurants
- Suivi de l'activité

---

## 🛠️ Stack Technique

| Composant | Technologies |
|-----------|--------------|
| **Frontend** | React / React Native |
| **Backend** | Django + Django REST Framework |
| **Base de données** | PostgreSQL |
| **IA** | Python (analyse budget, préférences, suggestions) |

---

## 📂 Structure de la Base de Données

``
User
  ├── id
  ├── nom
  ├── téléphone
  ├── email
  ├── mot_de_passe
  └── rôle

Restaurant
  ├── id
  ├── nom
  ├── localisation
  ├── menu
  ├── statut
  └── photos

Plat
  ├── id
  ├── nom
  ├── prix
  ├── catégorie
  └── restaurant_id

Commande
  ├── id
  ├── user_id
  ├── statut
  ├── total
  └── adresse

Livraison
  ├── id
  ├── commande_id
  ├── livreur_id
  └── statut
``

### 🔑 États Possibles d'un Restaurant
- pending - En attente
- pproved - Validé
- ejected - Refusé
- suspended - Bloqué

---

## 📱 Bonus pour l'Afrique

- ☎️ Bouton Appeler le restaurant
- 💬 Bouton WhatsApp restaurant
- 🚀 Commande rapide sans livraison au début

---

## ⚙️ Installation & Setup

### 1️⃣ Créer un environnement virtuel

``ash
python -m venv venv
``

Pour activer l'environnement :

``ash
# Linux/Mac
source venv/bin/activate

# Windows PowerShell
venv\Scripts\Activate.ps1
``

### 2️⃣ Installer les dépendances

``ash
pip install -r requirements.txt
``

### 3️⃣ Lancer le serveur Django

``ash
python manage.py runserver
``

---

## 📌 Roadmap

- **Phase 1** : MVP (utilisateur + restaurant + admin)
- **Phase 2** : Livraison (livreurs, suivi en temps réel)
- **Phase 3** : IA avancée (suggestions personnalisées, optimisation des menus)

---

## 👥 Équipe R&D

| Rôle | Personne |
|------|----------|
| CEO | Mohamed |
| CTO | RODIM'S Dieuveil |
| COO | Junior |

---

## 🎯 Objectif

Lancer rapidement un MVP fonctionnel, adapté au marché africain, avec une expérience utilisateur simple et une validation sécurisée des restaurants.
