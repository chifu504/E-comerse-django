import json
from django.shortcuts import render, get_object_or_404
from .models import Category, Product,favoritos,Comentarios
from cart.forms import CartAddProductForm
from django.core.paginator import Paginator
from .recommender import Recommender
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category,slug=category_slug)
        products = products.filter(category=category)

    precio_min = request.GET.get('precio_min')
    precio_max = request.GET.get('precio_max')
    color = request.GET.get('color')
    talla = request.GET.get('talla')

    if precio_min and precio_max:
        products = products.filter(price__gte=precio_min, price__lte=precio_max)
    
    if color:
        products = products.filter(color=color)
    
    if talla:
        products = products.filter(talla=talla)

    paginator = Paginator(products, 8)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'category': category,
        'categories': categories,
        'products': page_obj,
    }

    return render(request,'shop/list.html',context)

#incluimos tambien el slug segun por el seo 
def product_detail(request, id, slug):
    product = get_object_or_404(Product,id=id,slug=slug,available=True)
    cart_product_form = CartAddProductForm()
    r = Recommender()
    recommended_products = r.suggest_products_for([product], 4)
    is_favorited = False  
    if request.user.is_authenticated:
        is_favorited = favoritos.objects.filter(user=request.user, producto=product).exists()
    comentarios = Comentarios.objects.filter(producto=product)

    return render(request, 'shop/detail.html', {
        'product': product,
        'cart_product_form': cart_product_form,
        'recommended_products': recommended_products,
        'is_favorited': is_favorited,
        'comentarios': comentarios
    })

@login_required
def mostrar_favoritos(request):
    user_favorites = favoritos.objects.filter(user=request.user)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/favoritos.html', {'user_favorites': user_favorites,'cart_product_form': cart_product_form})



def favoritos_view(request):
     is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
     if not request.user.is_authenticated:
        return JsonResponse({'message': 'No autenticado'}, status=401)
     if request.method == 'POST' and is_ajax:
         data = json.loads(request.body)
         content = int(data.get('product_id_body'))
         product = get_object_or_404(Product, id=content)
         user = request.user

         favorito_existente = favoritos.objects.filter(user=user, producto=product).first()
        
         if favorito_existente:
            favoritos.objects.filter(user=user, producto=product).delete()
            return JsonResponse({'message': 'Quitar de favoritos', 'is_favorite': False})
         else:
            favoritos.objects.create(user=user, producto=product)
            return JsonResponse({'message': 'Agregar a favoritos', 'is_favorite': True})
     else:
        return JsonResponse({'message': 'Error'}, status=400)
     

def eliminar_favorito(request, favorite_id):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if request.method == 'DELETE' and is_ajax:
        favorite = get_object_or_404(favoritos, id=favorite_id, user=request.user)
        favorite.delete()
        return JsonResponse({'message': 'Favorito eliminado'}, status=200)
    else:
        return JsonResponse({'message': 'Error al eliminar el favorito'}, status=400)
    

def add_comment(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if not request.user.is_authenticated:
        return JsonResponse({'message': 'No autenticado'}, status=401)
    if request.method == 'POST' and is_ajax:
        data = json.loads(request.body)
        comment_text = data.get('commentText')
        product_id = data.get('productId')

        product = get_object_or_404(Product, id=product_id)

        comentario = Comentarios.objects.create(user=request.user, producto=product, review=comment_text)

        response_data = {
            'comment': comentario.review,
            'user': comentario.user.username,
            'creacion': comentario.creacion.strftime('%B %d, %Y, %I:%M %p')
        }
        return JsonResponse(response_data)
    else:
        return JsonResponse({'message': 'Error'}, status=400)


