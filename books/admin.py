from django.contrib import admin
from .models import Book, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'seller', 'category', 'condition', 'price', 'status', 'posted_at']
    list_filter = ['status', 'category', 'condition']
    search_fields = ['title', 'author']
    list_editable = ['status']
    actions = ['mark_as_sold']

    def mark_as_sold(self, request, queryset):
        queryset.update(status='sold')
    mark_as_sold.short_description = "Mark selected books as sold"