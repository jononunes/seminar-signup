# Generated by Django 3.2.6 on 2021-08-19 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0008_alter_person_cellphone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationError',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('error_description', models.TextField(blank=True)),
                ('notification_post_info', models.TextField(blank=True)),
                ('time_registered', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='person',
            name='cellphone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='email_address',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]
