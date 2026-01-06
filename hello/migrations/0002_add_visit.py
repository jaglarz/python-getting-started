# hello/migrations/0002_add_visit.py
from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
        ("hello", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Visit",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
