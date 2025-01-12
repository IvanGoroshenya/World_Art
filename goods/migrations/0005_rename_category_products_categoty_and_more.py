# Generated by Django 4.2.7 on 2024-03-04 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0004_rename_categoty_products_category_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='category',
            new_name='categoty',
        ),
        migrations.AlterField(
            model_name='products',
            name='discount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=7, verbose_name='Скидка в %'),
        ),
    ]
