# Generated by Django 3.0.4 on 2020-04-18 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0108_bidwons'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bidwons',
            name='slug',
            field=models.SlugField(default=0),
        ),
    ]
