from django.conf import settings
from django.db import models


class OrderStatusChoices(models.TextChoices):
    """Статусы заказов."""

    class Meta:
        verbose_name = 'статус объявления'


    OPEN = "OPEN", "Открыто"
    CLOSED = "CLOSED", "Закрыто"
    SERVICE = "SERVIE", "Обслуживается"


class Orders(models.Model):
    """Заказы"""
    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'

    name_order = models.TextField()
    description = models.TextField(default='')
    status = models.TextField(
        choices=OrderStatusChoices.choices,
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    service_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name_order

class Items(models.Model):
    """Товары"""

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

    order = models.ForeignKey(Orders, on_delete=models.CASCADE,)
    stroka = models.TextField(default='')
    count = models.IntegerField()

    #draft = models.BooleanField(default=True)

    def __str__(self):
        return "id: " + str(self.id) + ", товар: " + str(self.stroka) + ", count: " + self.count


# class FavouriteAdv(models.Model):
#     """ избранные объявления"""
#     class Meta:
#         verbose_name = 'избранное'
#         verbose_name_plural = 'избранные'
#
#     fav_adv = models.ForeignKey(Advertisement, related_name='adv', on_delete=models.CASCADE, verbose_name='обявление')
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
#
#     def __str__(self):
#         return str(self.user)