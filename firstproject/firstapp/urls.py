from django.urls import path
from firstapp import views 

urlpatterns = [
    path('hello/',views.display),
    path('datetime/',views.displaydatetime)
]
