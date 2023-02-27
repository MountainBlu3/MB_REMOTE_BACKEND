# Generated by Django 4.1.7 on 2023-02-27 12:17

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('staff_id', models.CharField(default=0, max_length=100, primary_key=True, serialize=False, unique=True)),
                ('phonenumber', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('email_address', models.EmailField(max_length=254)),
                ('department', models.CharField(choices=[('ADMIN', 'Administration'), ('IT', 'Information Technology'), ('MEDIA', 'Media')], max_length=100)),
                ('gender', models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female')], max_length=100)),
                ('state_of_origin', models.CharField(max_length=234)),
                ('account_number', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('^\\d+$', 'Enter a valid account number')])),
                ('bank', models.CharField(max_length=100)),
                ('account_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('staff', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='admin_staff', serialize=False, to='member.staff')),
                ('specialization', models.CharField(default='unassigned', max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='IT',
            fields=[
                ('staff', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='it_staff', serialize=False, to='member.staff')),
                ('specialization', models.CharField(default='unassigned', max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('staff', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='media_staff', serialize=False, to='member.staff')),
                ('specialization', models.CharField(default='unassigned', max_length=100, null=True)),
            ],
        ),
    ]
