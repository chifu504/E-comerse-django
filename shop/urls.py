from django.urls import path
from . import views
app_name = 'shop'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('favorito/',views.favoritos_view,name='favoritos'),
     path('mostrar_favoritos/',views.mostrar_favoritos,name='mostrar_favoritos'),
     path('add-comment/', views.add_comment, name='add_comment'),
     path('eliminar-favorito/<int:favorite_id>/',views.eliminar_favorito, name='eliminar_favorito'),
    path('<slug:category_slug>/', views.product_list,name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail,name='product_detail'),
       
]