# Generated by Django 2.2.9 on 2020-02-22 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0039_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='type',
            name='con',
            field=models.BooleanField(default=False),
        ),
    ]