# Generated by Django 3.2.6 on 2021-08-10 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0003_registration_registered_seminars'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='registration',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='database.registration'),
            preserve_default=False,
        ),
    ]
