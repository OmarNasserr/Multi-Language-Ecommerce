# Generated by Django 4.1.7 on 2023-03-04 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productvariations",
            name="product_color",
            field=models.ManyToManyField(
                related_name="product_variations", to="products_app.productcolor"
            ),
        ),
    ]
