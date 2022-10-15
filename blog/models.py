from django.conf import settings
from django.db import models
from django.utils import timezone

class Currency(models.Model):
    name = models.CharField('Валюта', max_length=200)

    def __str__(self):
        return self.name

class Post(models.Model):
    product = models.CharField('Продукт', max_length=200)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, verbose_name='Валюта')
    balance_users = models.IntegerField('Баланс юзеров продукта', null=True, blank=True)
    balance_reserve_fund = models.IntegerField('Баланс резервного фонда продукта', null=True, blank=True)
    description = models.TextField('Описание')
    archive = models.BooleanField('В архиве', default=False)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.product