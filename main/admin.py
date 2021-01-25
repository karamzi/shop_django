from django.contrib import admin
from main.models import Balls, Bags, Shoes, ShoesSize, Accessories, BallWeight, Cart, Orders


class BasicAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'price', 'availability',)
    list_display_links = ('name', 'company', 'price',)
    list_editable = ('availability',)
    readonly_fields = ('vendor_code',)


class AccessoriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'price', 'availability',)
    list_display_links = ('name', 'type', 'price',)
    list_editable = ('availability',)
    readonly_fields = ('vendor_code',)


class CartAdmin(admin.TabularInline):
    model = Cart
    readonly_fields = ('vendor_code', 'name', 'size', 'quantity', 'price')
    extra = 0


class OrdersAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'total_price', 'date')
    list_display_links = ('name', 'phone', 'total_price', 'date')
    readonly_fields = ('name', 'phone', 'email', 'total_price')
    inlines = [CartAdmin]


admin.site.register(Bags, BasicAdmin)
admin.site.register(Balls, BasicAdmin)
admin.site.register(Shoes, BasicAdmin)
# admin.site.register(ShoesSize)
admin.site.register(Accessories, AccessoriesAdmin)
# admin.site.register(BallWeight)
admin.site.register(Orders, OrdersAdmin)
