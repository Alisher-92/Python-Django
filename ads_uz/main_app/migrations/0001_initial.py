# Generated by Django 4.1.4 on 2022-12-11 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Описания товара')),
                ('preview', models.ImageField(upload_to='product-images', verbose_name='Фото товара')),
                ('price', models.FloatField(blank=True, null=True, verbose_name='Цена товара')),
                ('published', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата объявления')),
                ('contact_data', models.CharField(max_length=50, verbose_name='Контактные данные')),
            ],
        ),
    ]
