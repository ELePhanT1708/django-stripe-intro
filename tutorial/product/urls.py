from django.urls import path

from .views import (CancelView,
                    ProductLandingPageView,
                    SuccessView,
                    CreateCheckoutSessionView,
                    CreateIntentPayment
                    )

urlpatterns = [
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('items/', ProductLandingPageView.as_view(), name='items'),
    path('success/', SuccessView.as_view(), name='success'),
    path('create-checkout-session/<stripe_product_id>/', CreateCheckoutSessionView.as_view(),
         name='create-checkout-session'),
    path('create-intent-payment/<stripe_product_id>/', CreateIntentPayment.as_view(),
         name='create-intent-payment')
]
