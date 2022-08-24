from django.contrib import admin

from register.models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'cpf', 'phone', 'address',)
    list_display_links = ('full_name', 'phone',)
    list_filter = ('name', 'surname', 'phone',)
    ordering = ('-id',)
