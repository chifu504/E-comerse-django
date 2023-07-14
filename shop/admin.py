from django.contrib import admin
from .models import Category, Product,favoritos,Comentarios
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class ProductResource(resources.ModelResource):
    class Meta:
        model = Product



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)} 

@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    list_display = ['name', 'slug', 'price','available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}
    resource_class = ProductResource

@admin.register(favoritos)
class favoritosadmin(admin.ModelAdmin):
    list_display = ['id','user','producto','creacion']

    
@admin.register(Comentarios)
class Comentariosadmin(admin.ModelAdmin):
    list_display = ['id','user','producto','review','creacion']