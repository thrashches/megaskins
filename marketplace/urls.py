from django.urls import path
from .views import MainPage, CatalogListView, OrderCreateView

urlpatterns = [
    path('', MainPage.as_view(), name='index'),
    path('catalog/', CatalogListView.as_view(), name='catalog'),
    path('<int:pk>/order_create/', OrderCreateView.as_view(), name='order_create'),
]
