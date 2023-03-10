# Generated by Django 3.0.4 on 2020-04-18 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0110_bidwons_created_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bidwons',
            name='prod_id',
        ),
        migrations.AddField(
            model_name='bidwons',
            name='auction_status',
            field=models.CharField(default='F', max_length=10),
        ),
        migrations.AddField(
            model_name='bidwons',
            name='p_disc',
            field=models.TextField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='bidwons',
            name='p_loc',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='bidwons',
            name='p_title',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='bidwons',
            name='pimage',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]
