# Generated by Django 3.2.8 on 2022-02-08 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0007_appointment'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='form.patient'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='Starttime_of_appointment',
            field=models.TimeField(blank=True, max_length=50, verbose_name='Start-time of appointment '),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='date_of_appointment',
            field=models.DateField(blank=True, max_length=50, verbose_name='Date of appointment '),
        ),
    ]
