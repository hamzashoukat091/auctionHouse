# Generated by Django 3.0.4 on 2020-04-12 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0069_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
