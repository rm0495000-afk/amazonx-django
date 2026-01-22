from django.urls import path
from . import views

app_name = "amazon"

urlpatterns = [

    # 🏠 HOME
    path("", views.index, name="home"),

    # 🔐 AUTH
    path("login/", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path("logout/", views.logout_view, name="logout"),

    # 📦 PRODUCTS
    path("products/", views.product_list, name="product_list"),
    path("products/<int:product_id>/", views.product_detail, name="product_detail"),

    # 🛒 CART
    path("cart/", views.cart_detail, name="cart_detail"),
    path("add-to-cart/<int:product_id>/", views.add_to_cart, name="add_to_cart"),
    path("remove-from-cart/<int:product_id>/", views.remove_from_cart, name="remove_from_cart"),
    path("clear-cart/", views.clear_cart, name="clear_cart"),

    # ❤️ WISHLIST  🔥 (IMPORTANT – TRAILING SLASH)
    path("wishlist/", views.wishlist, name="wishlist"),
    path("wishlist/add/<int:product_id>/", views.add_to_wishlist, name="add_to_wishlist"),
    path("wishlist/remove/<int:product_id>/", views.remove_from_wishlist, name="remove_from_wishlist"),

    # 📦 ORDERS
    path("checkout/", views.checkout, name="checkout"),
    path("my-orders/", views.my_orders, name="my_orders"),

    # ℹ️ STATIC PAGES
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
]
