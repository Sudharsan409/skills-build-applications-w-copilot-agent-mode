# Generated by Django 4.1 on 2025-04-08 16:49

from django.db import migrations, models
import django.db.models.deletion
import octofit_tracker.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Team",
            fields=[
                (
                    "id",
                    models.CharField(
                        default=octofit_tracker.models.generate_object_id,
                        max_length=24,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.CharField(
                        default=octofit_tracker.models.generate_object_id,
                        max_length=24,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("name", models.CharField(max_length=255)),
                ("age", models.IntegerField()),
                ("team", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Workout",
            fields=[
                (
                    "id",
                    models.CharField(
                        default=octofit_tracker.models.generate_object_id,
                        max_length=24,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("duration", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Leaderboard",
            fields=[
                (
                    "id",
                    models.CharField(
                        default=octofit_tracker.models.generate_object_id,
                        max_length=24,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("points", models.IntegerField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="octofit_tracker.user",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Activity",
            fields=[
                (
                    "id",
                    models.CharField(
                        default=octofit_tracker.models.generate_object_id,
                        max_length=24,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("activity_type", models.CharField(max_length=255)),
                ("duration", models.IntegerField()),
                ("date", models.DateField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="octofit_tracker.user",
                    ),
                ),
            ],
        ),
    ]
