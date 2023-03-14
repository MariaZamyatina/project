from django.contrib import admin

from proizvodstvo.models import Orders


@admin.register(Orders)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_order', 'description', 'status', 'created_at', 'service_at']

#
# @admin.register(FavouriteAdv)
# class FavouriteAdvAdmin(admin.ModelAdmin):
#     list_display = ['id', 'user', 'fav_adv',]

