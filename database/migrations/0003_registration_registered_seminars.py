# Generated by Django 3.2.6 on 2021-08-10 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_seminar_capacity'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='registered_seminars',
            field=models.ManyToManyField(to='database.Seminar'),
        ),
    ]