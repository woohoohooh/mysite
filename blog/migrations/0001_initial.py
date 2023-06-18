# Generated by Django 4.1.2 on 2022-10-27 05:18

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Валюта')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=200, verbose_name='Продукт')),
                ('balance_users', models.IntegerField(blank=True, null=True, verbose_name='Баланс юзеров продукта')),
                ('balance_reserve_fund', models.IntegerField(blank=True, null=True, verbose_name='Баланс резервного фонда продукта')),
                ('description', models.TextField(verbose_name='Описание')),
                ('archive', models.BooleanField(default=False, verbose_name='В архиве')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.currency', verbose_name='Валюта')),
            ],
        ),
    ]
