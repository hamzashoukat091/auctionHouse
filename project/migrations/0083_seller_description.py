# Generated by Django 3.0.4 on 2020-04-14 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0082_buyer'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='description',
            field=models.TextField(default='', max_length=500),
        ),
    ]