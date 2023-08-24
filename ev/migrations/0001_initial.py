# Generated by Django 4.2.4 on 2023-08-24 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="EV",
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
                ("name", models.CharField(max_length=255)),
                ("manufacturer", models.CharField(max_length=255)),
                ("battery_size", models.IntegerField()),
                ("wltp_range", models.IntegerField()),
                ("cost", models.IntegerField()),
                ("power", models.IntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]