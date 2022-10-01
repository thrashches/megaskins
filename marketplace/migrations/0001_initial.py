# Generated by Django 4.1.1 on 2022-09-30 20:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('in_stock', models.BooleanField(default=True, verbose_name='Наличие')),
                ('image', models.ImageField(upload_to='goods', verbose_name='Изображение товара')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('new', 'Новый'), ('payed', 'Оплачен'), ('canceled', 'Отменен')], default='new', max_length=10, verbose_name='Статус заказа')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketplace.product', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
    ]
