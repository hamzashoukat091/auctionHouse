# Generated by Django 2.2.9 on 2020-02-23 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0047_call_for_interview_intoresume_job_recommended'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
