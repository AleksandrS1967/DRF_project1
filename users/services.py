import os
import stripe
from config.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY


def create_stripe_product(product):
    """Создает продукт в stripe(урок или курс)"""

    title_product = (
        product.paid_course if product.paid_course else product.paid_lesson
    )
    stripe_product = stripe.Product.create(name=f"{title_product}")
    return stripe_product.get("id")


def create_stripe_price(amount, product_id):
    """Создает цену в stripe"""

    return stripe.Price.create(
        currency="usd",
        unit_amount=amount * 100,
        product=product_id,
    )


def create_stripe_session(price):
    """Создает сессию на оплату в stripe"""

    session = stripe.checkout.Session.create(
        success_url="https://127.0.0.1:8000",
        line_items=[{"price": price.get("id"), "quantity": 1}],
        mode="payment",
    )
    return session.get("id"), session.get("url")