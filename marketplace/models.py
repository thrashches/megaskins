from django.db import models


class Product(models.Model):
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    name = models.CharField(max_length=255, verbose_name='Название')
    price = models.DecimalField(max_digits=10, decimal_places=2,
                                verbose_name='Цена')
    in_stock = models.BooleanField(default=True, verbose_name='Наличие')
    image = models.ImageField(upload_to='img',
                              verbose_name='Изображение товара')

    def __str__(self):
        return f'{self.name} {self.price}'


class Order(models.Model):
    NEW = 'new'
    PAYED = 'payed'
    CANCELED = 'canceled'

    STATUS_CHOICES = [
        (NEW, 'Новый'),
        (PAYED, 'Оплачен'),
        (CANCELED, 'Отменен'),
    ]

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                verbose_name='Товар')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES,
                              default=NEW, verbose_name='Статус заказа')

    def __str__(self):
        return f'{self.id} {self.status}'

    @property
    def price(self):
        return self.product.price

    @property
    def description(self):
        return self.product.name
