# Generated by Django 3.0.2 on 2020-02-11 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0024_intoresume_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
