from django.db import models

# Create your models here.
from authnapp.models import ShopUser
from product.models import Product

# class BasketQuerySet(models.QuerySet):
#     def delete(self, *args, **kwargs):
#         for item in self:
#             item.product.quantity += item.quantity
#             item.product.save()
#
#         super(BasketQuerySet, self).delete(*args, **kwargs)

class Basket(models.Model):
    # objects = BasketQuerySet.as_manager()

    user = models.ForeignKey(ShopUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    create_timestamp = models.DateTimeField(auto_now_add=True)
    update_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Корзина для {self.user.username} | Продукт {self.product.name}'

    def summ(self):
        return self.quantity * self.product.price

    def total_summ(self):
        baskets = Basket.objects.filter(user=self.user)
        return sum(basket.summ() for basket in baskets)

    def total_quantity(self):
        baskets = Basket.objects.filter(user=self.user)
        return sum(basket.quantity for basket in baskets)

    # def delete(self, using=None, keep_parents=False, *args, **kwargs):
    #     super(Basket, self).delete(*args, **kwargs)
    #     self.product.quantity += self.quantity
    #     self.save()
    #
    #
    # def save(self, force_insert=False, force_update=False, using=None,
    #          update_fields=None, *args, **kwargs):
    #     if self.pk:
    #         get_item = instance.get_item(int(instance.pk))
    #         instance.product.quantity -= instance.quantity - get_item
    #
    #     else:
    #         self.product.quantity -= self.quantity
    #     self.product.save()
    #     super(Basket, self).save(*args, **kwargs)
    #
    @staticmethod
    def get_item(pk):
        return Basket.objects.get(pk=pk).quantity