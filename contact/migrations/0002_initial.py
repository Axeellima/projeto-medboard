# Generated by Django 4.1.5 on 2023-01-10 14:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("hospital", "0001_initial"),
        ("patient", "0001_initial"),
        ("contact", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="contact",
            name="employee",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="contact",
            name="hospital",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to="hospital.hospital"
            ),
        ),
        migrations.AddField(
            model_name="contact",
            name="patient",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to="patient.patient"
            ),
        ),
    ]
