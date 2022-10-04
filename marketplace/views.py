import requests
from django.views import generic
from django.conf import settings
from django.shortcuts import get_object_or_404, render
from .models import Product, Order


class MainPage(generic.TemplateView):
    template_name = 'index.html'


class CatalogListView(generic.ListView):
    template_name = 'catalog.html'
    model = Product

    def get_queryset(self):
        return super().get_queryset().filter(in_stock=True)


class OrderCreateView(generic.DetailView):
    template_name = 'order_create.html'
    model = Product
    extra_context = {
        'payment_url': settings.PAYLER_SERVER + '/gapi/Pay'
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order = Order.objects.create(product=self.get_object())
        order.save()
        response = requests.post(
            url=settings.PAYLER_SERVER + '/gapi/StartSession',
            data={
                "key": settings.PAYLER_PAYMENT_KEY,
                "order_id": order.id,
                "amount": order.amount,
                "type": "OneStep",
                "session_type": 0,
                "product": self.object.name,
                "lang": "ru"
            }
        )
        response_json = response.json()
        context['session_id'] = response_json.get('session_id')
        context['order'] = order
        return context


class FinishTemplateView(generic.TemplateView):
    template_name = 'finish.html'

    def get_order_id(self):
        order_id = self.request.GET.get('order_id')
        return order_id

    def get_order(self):
        order = get_object_or_404(Order, id=self.get_order_id())
        return order

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        response = requests.post(
            url=settings.PAYLER_SERVER + '/gapi/GetStatus',
            data={
                'key': settings.PAYLER_PAYMENT_KEY,
                'order_id': self.get_order_id()
            }
        )
        response_json = response.json()
        order = self.get_order()
        if response_json.get('status') == 'Charged':
            order.status = order.PAYED
            order.save()
            status = "оплачен"
        else:
            status = 'не оплачен'
        context['status'] = status
        return context
