# Generated by Django 3.2.6 on 2021-08-14 15:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0005_registration_additional_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='time_registered',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
