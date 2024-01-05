# Generated by Django 4.1.1 on 2023-10-15 12:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("tags", "__first__"),
    ]

    operations = [
        migrations.CreateModel(
            name="Job",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=300)),
                ("description", models.TextField()),
                ("location", models.CharField(max_length=150)),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("1", "Full time"),
                            ("2", "Part time"),
                            ("3", "Internship"),
                        ],
                        max_length=10,
                    ),
                ),
                ("category", models.CharField(max_length=100)),
                ("last_date", models.DateTimeField()),
                ("company_name", models.CharField(max_length=100)),
                ("company_description", models.CharField(max_length=300)),
                ("website", models.CharField(default="", max_length=100)),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                ("filled", models.BooleanField(default=False)),
                ("salary", models.IntegerField(blank=True, default=0)),
                ("vacancy", models.IntegerField(default=1)),
                ("tags", models.ManyToManyField(to="tags.tag")),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["id"],
            },
        ),
        migrations.CreateModel(
            name="Favorite",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                ("soft_deleted", models.BooleanField(default=False)),
                (
                    "job",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="favorites",
                        to="jobsapp.job",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Applicant",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                ("comment", models.TextField(blank=True, null=True)),
                ("status", models.SmallIntegerField(default=1)),
                (
                    "job",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="applicants",
                        to="jobsapp.job",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["id"],
                "unique_together": {("user", "job")},
            },
        ),
    ]