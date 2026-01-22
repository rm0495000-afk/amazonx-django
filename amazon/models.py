from django.db import models
from django.contrib.auth.models import User
from cloudinary_storage.storage import MediaCloudinaryStorage

# 🔥 FORCE Cloudinary storage
cloudinary_storage = MediaCloudinaryStorage()


# ===============================
# 📦 PRODUCT MODEL
# ===============================
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()

    # 🔥 IMAGE FORCE CLOUDINARY
    image = models.ImageField(
        storage=cloudinary_storage,
        upload_to="products/",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name


# ===============================
# ⭐ PRODUCT REVIEWS
# ===============================
class Review(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="reviews"
    )
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} - {self.rating}⭐"


# ===============================
# 📦 ORDER MODEL
# ===============================
class Order(models.Model):
    STATUS_CHOICES = [
        ("PLACED", "Placed"),
        ("SHIPPED", "Shipped"),
        ("DELIVERED", "Delivered"),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    total_amount = models.IntegerField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="PLACED"
    )

    def __str__(self):
        return f"Order #{self.id} ({self.status})"


# ===============================
# 📦 ORDER ITEM
# ===============================
class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        related_name="items",
        on_delete=models.CASCADE
    )
    product_name = models.CharField(max_length=200)
    price = models.IntegerField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.product_name


# ===============================
# 💸 COUPON
# ===============================
class Coupon(models.Model):
    code = models.CharField(max_length=20, unique=True)
    discount_percent = models.IntegerField()

    def __str__(self):
        return f"{self.code} ({self.discount_percent}%)"


# ===============================
# ❤️ WISHLIST
# ===============================
class Wishlist(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "product")

    def __str__(self):
        return f"{self.product.name} in wishlist"
