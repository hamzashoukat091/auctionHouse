# Generated by Django 3.0.4 on 2020-04-12 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0070_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='prod_files',
        ),
    ]