# Generated by Django 3.0.4 on 2020-04-14 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0087_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='buy',
        ),
    ]