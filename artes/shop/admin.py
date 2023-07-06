from mptt.admin import DraggableMPTTAdmin

from django.contrib import admin

from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'photo_s')
    list_display_links = ('id', 'title', 'photo_s')
    search_fields = ('title',)
    list_filter = ('price',)
    prepopulated_fields = {'slug':('title',)}
    exclude = ('photo_s', 'photo_m', 'photo_l')

class CategoryAdmin(DraggableMPTTAdmin):
    tree_title_field = 'name'
    tree_display = ('id', 'name')
    # list_display = ('id', 'name')
    # list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('name',)
    prepopulated_fields = {'slug':('name',)}
    exclude = ('parent',)

    class Meta:
        model = Category

class SubcategoryAdmin(DraggableMPTTAdmin):
    tree_title_field = 'name'
    tree_display = ('id', 'name')
    # list_display = ('id', 'name', 'parent')
    # list_display_links = ('id', 'name')
    search_fields = ('name', 'parent')
    list_filter = ('parent',)
    prepopulated_fields = {'slug':('name',)}

    class Meta:
        model = Subcategory

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)