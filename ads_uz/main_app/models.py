from django.db import models
from accounts_app.models import CustomerUser


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    content = models.TextField(null=True, blank=True, verbose_name="Описания товара")
    preview = models.ImageField(upload_to="product-images", verbose_name="Фото товара")
    price = models.FloatField(null=True, blank=True, verbose_name="Цена товара")
    published = models.DateTimeField(auto_now_add=True,
                                     db_index=True, verbose_name="Дата объявления")
    contact_data = models.CharField(max_length=50, verbose_name="Номер телефона")
    category = models.ForeignKey("Category", null=True,
                                 on_delete=models.PROTECT, verbose_name="Рубрика")
    author = models.ForeignKey(CustomerUser, on_delete=models.CASCADE,
                               verbose_name="Автор", default=1)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Объявления"
        verbose_name_plural = "Объявлении"


class Category(models.Model):
    name = models.CharField("Рубрика", max_length=30)
    slug = models.SlugField("Тег", unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Рубрика"
        verbose_name_plural = "Рубрики"
        ordering = ["pk"]
