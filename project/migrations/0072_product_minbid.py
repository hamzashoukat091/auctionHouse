# Generated by Django 3.0.4 on 2020-04-12 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0071_remove_product_prod_files'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='minbid',
            field=models.FloatField(default=0.0),
        ),
    ]
