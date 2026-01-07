from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import (
    Product,
    Order,
    OrderItem,
    Coupon,
    Review,
    Wishlist
)
from .cart_utils import Cart


# =========================
# 🔐 AUTH VIEWS
# =========================

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)

            # 🔥 Admin → admin panel
            if user.is_superuser:
                return redirect("/admin/")

            # 👤 User → product list
            return redirect("amazon:product_list")

        messages.error(request, "Invalid username or password")
        return redirect("amazon:login")

    return render(request, "amazon/login.html")


def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("amazon:register")

        user = User.objects.create_user(
            username=username,
            password=password
        )
        login(request, user)
        return redirect("amazon:product_list")

    return render(request, "amazon/register.html")


def logout_view(request):
    logout(request)
    return redirect("amazon:login")


# =========================
# 🏠 HOME
# =========================
def index(request):
    return render(request, "amazon/index.html")


# =========================
# 📦 PRODUCT LIST + SEARCH
# =========================
def product_list(request):
    q = request.GET.get("q", "")
    products = Product.objects.filter(name__icontains=q).order_by("-id")

    return render(request, "amazon/product_list.html", {
        "products": products,
        "search_query": q
    })


# =========================
# 🔍 PRODUCT DETAIL + REVIEWS
# =========================
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    reviews = Review.objects.filter(product=product)

    # 🔥 Recently viewed (session)
    recent = request.session.get("recent_products", [])
    if product.id not in recent:
        recent.insert(0, product.id)
    request.session["recent_products"] = recent[:5]

    recent_products = Product.objects.filter(id__in=recent)

    if request.method == "POST":
        Review.objects.create(
            product=product,
            rating=request.POST.get("rating"),
            comment=request.POST.get("comment")
        )
        return redirect("amazon:product_detail", product_id=product.id)

    return render(request, "amazon/detail.html", {
        "product": product,
        "reviews": reviews,
        "recent_products": recent_products
    })


# =========================
# ➕ ADD TO CART
# =========================
def add_to_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)

    cart.add(
        product_id=product.id,
        product_name=product.name,
        price=int(product.price),
        quantity=1
    )
    return redirect("amazon:cart_detail")


# =========================
# 🛒 CART
# =========================
def cart_detail(request):
    cart = Cart(request)
    return render(request, "amazon/cart.html", {
        "cart_items": cart.get_items(),
        "total": cart.get_total_price()
    })


def remove_from_cart(request, product_id):
    cart = Cart(request)
    cart.remove(product_id)
    return redirect("amazon:cart_detail")


def clear_cart(request):
    cart = Cart(request)
    cart.clear()
    return redirect("amazon:cart_detail")


# =========================
# ✅ CHECKOUT + COUPON + ORDER
# =========================
@login_required
def checkout(request):
    cart = Cart(request)
    total = cart.get_total_price()
    discount = 0
    message = ""

    if request.method == "POST":
        code = request.POST.get("coupon")

        if code:
            try:
                coupon = Coupon.objects.get(code=code)
                discount = coupon.discount_percent
            except Coupon.DoesNotExist:
                message = "Invalid coupon code"

        final_total = total - (total * discount // 100)

        order = Order.objects.create(
            user=request.user,
            total_amount=final_total
        )

        for item in cart.get_items():
            OrderItem.objects.create(
                order=order,
                product_name=item["name"],
                price=item["price"],
                quantity=item["quantity"]
            )

        cart.clear()
        return redirect("amazon:my_orders")

    return render(request, "amazon/checkout.html", {
        "cart_items": cart.get_items(),
        "total": total,
        "message": message
    })


# =========================
# 📦 MY ORDERS (USER ONLY)
# =========================
@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "amazon/my_orders.html", {
        "orders": orders
    })


# =========================
# ❤️ WISHLIST
# =========================
@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    Wishlist.objects.get_or_create(
        user=request.user,
        product=product
    )
    return redirect("amazon:wishlist")


@login_required
def wishlist(request):
    items = Wishlist.objects.filter(user=request.user)
    return render(request, "amazon/wishlist.html", {
        "items": items
    })


@login_required
def remove_from_wishlist(request, product_id):
    Wishlist.objects.filter(
        user=request.user,
        product_id=product_id
    ).delete()
    return redirect("amazon:wishlist")

def about(request):
    return render(request, 'amazon/about.html')


def contact(request):
    return render(request, 'amazon/contact.html')
