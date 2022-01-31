# Generated by Django 3.2.8 on 2022-01-31 12:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, null=True, verbose_name='First name')),
                ('last_name', models.CharField(max_length=20, null=True, verbose_name='Last_name')),
                ('role', models.CharField(max_length=20, null=True, verbose_name='Doctor/Patient')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('address_line1', models.CharField(blank=True, max_length=100, verbose_name='Address_Line1')),
                ('city', models.CharField(blank=True, max_length=50, verbose_name='City')),
                ('state', models.CharField(blank=True, max_length=50, verbose_name='State')),
                ('country', models.CharField(blank=True, max_length=50, verbose_name='Country')),
                ('pincode', models.CharField(blank=True, max_length=50, verbose_name='Pincode')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
