from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.

#créons la table catégorie
class Category(models.Model):
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_added'] #classons les catégories par ordre d'ajout

    def __str__(self):
        return self.name
        

#créons la table produit
class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()
    category = ForeignKey(Category, related_name='categorie', on_delete=models.CASCADE)
    image = models.CharField(max_length=5000)
    date_added = models.DateTimeField(auto_now=True)

    
    class Meta:
        ordering = ['-date_added'] #classons les produits par ordre d'ajout

    def __str__(self):
        return self.title

#créons la table commande
class Commande(models.Model):
    items = models.CharField(max_length=300)
    total = models.CharField(max_length=200)
    nom = models.CharField(max_length=150)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    ville = models.CharField(max_length=200)
    pays = models.CharField(max_length=300)
    zipcode = models.CharField(max_length=300)
    date_commande = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_commande']

    def __str__(self):
        return self.nom
    