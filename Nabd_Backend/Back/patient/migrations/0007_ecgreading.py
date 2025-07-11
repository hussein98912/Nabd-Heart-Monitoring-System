# Generated by Django 5.0.6 on 2024-06-18 22:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("patient", "0006_patient_signup_phone_number"),
    ]

    operations = [
        migrations.CreateModel(
            name="ECGReading",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("timestamp", models.DateTimeField()),
                ("value", models.FloatField()),
                (
                    "patient",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="patient.patient_signup",
                    ),
                ),
            ],
            options={
                "indexes": [
                    models.Index(
                        fields=["patient", "timestamp"],
                        name="patient_ecg_patient_c35111_idx",
                    )
                ],
            },
        ),
    ]
