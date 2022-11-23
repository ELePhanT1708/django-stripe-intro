from django.urls import path

from .views import (CancelView,
                    ProductLandingPageView,
                    SuccessView,
                    CreateCheckoutSessionView
                    )

urlpatterns = [
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('', ProductLandingPageView.as_view(), name='landing'),
    path('success/', SuccessView.as_view(), name='success'),
    path('create-checkout-session/<pk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session')
]
