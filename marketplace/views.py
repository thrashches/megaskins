from django.views import generic
from django.conf import settings
from django.shortcuts import get_object_or_404
from .models import Product, Order


class MainPage(generic.TemplateView):
    template_name = 'index.html'


class CatalogListView(generic.ListView):
    template_name = 'catalog.html'
    model = Product

    def get_queryset(self):
        return super().get_queryset().filter(in_stock=True)


class OrderCreateView(generic.CreateView):
    template_name = 'order_create.html'
    model = Order
    fields = []

    def form_valid(self, form):
        product = get_object_or_404(Product, id=self.kwargs.get('pk'))
        form.instance.product = product
        return super().form_valid(form)

    def get_success_url(self):
        start_session_url = settings.PAYLER_SERVER + '/gapi/StartSession'

        pass
