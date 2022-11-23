
from django.urls import path
from quoteapp import views 

urlpatterns = [
    path('displayQuote/',views.displayQuote)
]
