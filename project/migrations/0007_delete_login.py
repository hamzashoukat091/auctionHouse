# Generated by Django 2.2.7 on 2019-12-02 21:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_remove_login_nam'),
    ]

    operations = [
        migrations.DeleteModel(
            name='login',
        ),
    ]