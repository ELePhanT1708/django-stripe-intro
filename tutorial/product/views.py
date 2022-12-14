import json
from typing import List

import stripe
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import redirect
from django.views import View
from django.views.generic import TemplateView

from .models import Item

stripe.api_key = settings.STRIPE_SECRET_KEY


class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        product = Item.objects.get(stripe_product_id=self.kwargs["stripe_product_id"])
        domain = "https://yourdomain.com"
        if settings.DEBUG:
            domain = "http://127.0.0.1:8000"
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price': product.stripe_product_id,
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=domain + '/success/',
            cancel_url=domain + '/cancel/',
        )
        return redirect(checkout_session.url)


def calculate_order_amount(items: List[Item]):
    return [item.price for item in items].sum()


class CreateIntentPayment(View):

    def post(self, request, *args, **kwargs):
        try:
            product = Item.objects.get(stripe_product_id=self.kwargs["stripe_product_id"])
            # Create a PaymentIntent with the order amount and currency
            intent = stripe.PaymentIntent.create(
                amount=product.price,
                currency='usd',
                automatic_payment_methods={
                    'enabled': True,
                },
                description=product.description
            )
            return JsonResponse({
                'clientSecret': intent['client_secret']
            })
        except Exception as e:
            return JsonResponse({"error": str(e)})


class ProductLandingPageView(TemplateView):
    template_name = "landing.html"

    def get_context_data(self, **kwargs):
        products = Item.objects.all()
        context = super(ProductLandingPageView,
                        self).get_context_data(**kwargs)
        context.update({
            "products": products,
        })
        return context


class SuccessView(TemplateView):
    template_name = "success.html"


class CancelView(TemplateView):
    template_name = "cancel.html"