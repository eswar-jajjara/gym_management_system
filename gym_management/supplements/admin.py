from django.contrib import admin
from .models import ProductType, ProductCategory, Supplement


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon')


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'product_count')
    list_filter = ('type',)

    def product_count(self, obj):
        return obj.supplement_set.count()


@admin.register(Supplement)
class SupplementAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'category', 'price', 'stock_status', 'weight_goal')
    list_filter = ('type', 'category', 'weight_goal', 'is_diet_food')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}

    def stock_status(self, obj):
        return "In Stock" if obj.stock > 0 else "Out of Stock"