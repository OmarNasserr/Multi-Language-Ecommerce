# Generated by Django 4.1.7 on 2023-03-07 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("colors_app", "0001_initial"),
        ("products_app", "0004_productthumbnailimage"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productcolor",
            name="color",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="product_color",
                to="colors_app.color",
            ),
        ),
    ]
