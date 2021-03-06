# Generated by Django 3.2.6 on 2021-10-18 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0010_auto_20211018_2036'),
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('seminars', models.ManyToManyField(to='database.Seminar')),
            ],
        ),
    ]
