# Generated by Django 3.2.6 on 2021-08-18 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0006_registration_time_registered'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='seminar',
            options={'ordering': ['subject', 'level']},
        ),
        migrations.RemoveField(
            model_name='payment',
            name='amount_paid',
        ),
        migrations.AddField(
            model_name='payment',
            name='amount_fee',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='payment',
            name='amount_gross',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='payment',
            name='amount_net',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='payment',
            name='item_name',
            field=models.CharField(default='itemname', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='payment',
            name='m_payment_id',
            field=models.CharField(default='01', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='payment',
            name='payment_status',
            field=models.CharField(default='None', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='payment',
            name='pf_payment_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
