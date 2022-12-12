from django.db import models

from django.contrib.auth.models import AbstractUser
from django.core import validators


class CustomerUser(AbstractUser):
    age = models.PositiveSmallIntegerField("Возраст", validators=[
        validators.MaxValueValidator(120, message="Максимальное значение 120"),
        validators.MinValueValidator(16, message="Минимальный допустимый возраст регистрации 16 лет")
    ])
    phone_number = models.CharField("Номер телефона", max_length=15, validators=[
        validators.MinLengthValidator(6, message="Минимальная длина - 6 символов")
    ])

    REQUIRED_FIELDS = ["email", "age", "phone_number"]

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

