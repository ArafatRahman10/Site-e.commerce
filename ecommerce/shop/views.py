from django.shortcuts import render, redirect
from .models import Product, Commande
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    # Affichons les produits de notre BD
    product_object = Product.objects.all()
    #fonction qui recherche un produit dans la BD
    item_name = request.GET.get('item-name')
    if item_name !='' and item_name is not None:
        product_object = Product.objects.filter(title__icontains=item_name)
    #paginons la page d'affichage de nos produits
    paginator = Paginator(product_object, 4)
    page = request.GET.get('page')
    product_object = paginator.get_page(page)    
    return render(request, 'shop/index.html', {'product_object': product_object})

#fonction qui affiche les détails de chaque produit
def detail(request, myid):
    product_object = Product.objects.get(id=myid)
    return render(request, 'shop/detail.html', {'product': product_object}) 

#fonction qui affiche la page checkout des commandes 
def checkout(request):
    if request.method == "POST":
        items = request.POST.get('items')
        total = request.POST.get('total')
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        address = request.POST.get('address')
        ville = request.POST.get('ville')
        pays = request.POST.get('pays')
        phone = request.POST.get('phone')
        com = Commande(items=items, total=total, nom=nom, email=email, address=address, ville=ville, pays=pays, phone=phone)
        com.save()
        return redirect('confirmation')

    return render(request, 'shop/checkout.html') 

#fonction de confirmation de la commande du client
def confirmation(request):
    info = Commande.objects.all()[:1]
    for item in info:
        nom = item.nom    

    return render(request, 'shop/confirmation.html', {'name': nom})    
