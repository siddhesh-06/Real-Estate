from django.urls import path
from . import views # import all things

urlpatterns = [
    path('',views.index, name='listings'),
    path('<int:listing_id>',views.listing, name='listing'),
    path('search',views.search, name='search'),
]