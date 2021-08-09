# Generated by Django 3.2.6 on 2021-08-09 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_paid', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=40)),
                ('email_address', models.EmailField(max_length=254)),
                ('cellphone_number', models.CharField(max_length=11, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Seminar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(choices=[('MATHS_P1', 'Maths Paper 1'), ('MATHS_P2', 'Maths Paper 2'), ('PHYSICS', 'Physics'), ('CHEMISTRY', 'Chemistry')], max_length=15)),
                ('level', models.CharField(choices=[('STANDARD', 'Standard'), ('ADVANCED', 'Advanced')], max_length=15)),
                ('date_and_time', models.DateTimeField()),
                ('base_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('course_content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_guardian_accepts_waiver', models.BooleanField()),
                ('child_accepts_waiver', models.BooleanField()),
                ('child', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='child', to='database.person')),
                ('parent_guardian', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='parent_guardian', to='database.person')),
            ],
        ),
    ]
