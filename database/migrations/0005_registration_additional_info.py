# Generated by Django 3.2.6 on 2021-08-10 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0004_payment_registration'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='additional_info',
            field=models.TextField(blank=True, default=''),
        ),
    ]