from django.shortcuts import render
from .models import Product
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
    return render(request, 'shop/checkout.html')    