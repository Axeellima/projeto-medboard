# Generated by Django 4.1.5 on 2023-01-12 03:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("address", "0003_alter_address_cep_alter_address_number"),
    ]

    operations = [
        migrations.RenameField(
            model_name="address",
            old_name="cep",
            new_name="zipcode",
        ),
    ]
