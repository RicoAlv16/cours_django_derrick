# Generated by Django 5.1.2 on 2024-10-16 14:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="livre",
            name="editeur",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="books_app.editeur",
            ),
            preserve_default=False,
        ),
    ]
