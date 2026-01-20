from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Product, Review, Order, OrderItem, Coupon


# ===============================
# 📦 PRODUCT ADMIN
# ===============================
@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ("name", "price")
    search_fields = ("name",)
    list_filter = ("price",)
    ordering = ("name",)


# ===============================
# ⭐ REVIEW ADMIN
# ===============================
@admin.register(Review)
class ReviewAdmin(ModelAdmin):
    list_display = ("product", "rating", "created_at")
    list_filter = ("rating", "created_at")
    search_fields = ("product__name",)


# ===============================
# 📦 ORDER ITEM INLINE (FIXED)
# ===============================
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ("price", "quantity")   # ✅ FIX


# ===============================
# 📦 ORDER ADMIN
# ===============================
@admin.register(Order)
class OrderAdmin(ModelAdmin):
    list_display = ("id", "total_amount", "status", "created_at")
    list_filter = ("status", "created_at")
    list_editable = ("status",)
    ordering = ("-created_at",)
    inlines = [OrderItemInline]


# ===============================
# 💸 COUPON ADMIN
# ===============================
@admin.register(Coupon)
class CouponAdmin(ModelAdmin):
    list_display = ("code", "discount_percent")
    search_fields = ("code",)
    list_filter = ("discount_percent",)
