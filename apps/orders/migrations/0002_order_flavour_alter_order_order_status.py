# Generated by Django 4.0.4 on 2022-05-05 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="flavour",
            field=models.CharField(default="", max_length=50),
        ),
        migrations.AlterField(
            model_name="order",
            name="order_status",
            field=models.CharField(
                choices=[
                    ("PENDING", "Pending"),
                    ("IN_TRANSIT", "In Transit"),
                    ("DELIVERED", "Delivered"),
                ],
                default="PENDING",
                max_length=20,
            ),
        ),
    ]
