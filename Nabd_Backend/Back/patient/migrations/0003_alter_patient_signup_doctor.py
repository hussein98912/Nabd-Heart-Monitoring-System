# Generated by Django 5.0.2 on 2024-05-06 14:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0007_remove_signup_username_signup_address_signup_age_and_more'),
        ('patient', '0002_patient_signup_doctor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient_signup',
            name='doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='doctor.doctorprofile'),
        ),
    ]
