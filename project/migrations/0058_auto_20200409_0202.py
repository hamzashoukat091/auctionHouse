# Generated by Django 3.0.4 on 2020-04-08 21:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0057_auto_20200227_1837'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='intoresume',
            name='user',
        ),
        migrations.RemoveField(
            model_name='job',
            name='user',
        ),
        migrations.RemoveField(
            model_name='recommended',
            name='user',
        ),
        migrations.RemoveField(
            model_name='type',
            name='user',
        ),
        migrations.DeleteModel(
            name='FeedBack',
        ),
        migrations.DeleteModel(
            name='intoresume',
        ),
        migrations.DeleteModel(
            name='Job',
        ),
        migrations.DeleteModel(
            name='recommended',
        ),
        migrations.DeleteModel(
            name='Type',
        ),
    ]
