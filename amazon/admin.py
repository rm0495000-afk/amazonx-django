from django.contrib import admin
from .models import Product, Review, Order, OrderItem, Coupon


# ===============================
# 📦 PRODUCT ADMIN
# ===============================
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)
    list_filter = ('price',)
    ordering = ('name',)


# ===============================
# ⭐ REVIEW ADMIN
# ===============================
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('product__name',)


# ===============================
# 📦 ORDER ITEM INLINE (ADVANCED)
# ===============================
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ('product_name', 'price', 'quantity')


# ===============================
# 📦 ORDER ADMIN (FEATURE 8)
# ===============================
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'total_amount', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    list_editable = ('status',)   # 🔥 STATUS CHANGE DIRECTLY
    ordering = ('-created_at',)
    inlines = [OrderItemInline]


# ===============================
# 💸 COUPON ADMIN (FEATURE 9)
# ===============================
@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount_percent')
    search_fields = ('code',)
    list_filter = ('discount_percent',)
