from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("estimates", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="inquiry",
            name="user_context",
        ),
        migrations.AddField(
            model_name="inquiry",
            name="current_property",
            field=models.TextField(default=""),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="inquiry",
            name="property_goal",
            field=models.TextField(default=""),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="inquiry",
            name="investment_commitment",
            field=models.TextField(default=""),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="inquiry",
            name="excitement_notes",
            field=models.TextField(default=""),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="inquiry",
            name="updated_at",
            field=models.DateTimeField(default=django.utils.timezone.now, auto_now=True),
            preserve_default=False,
        ),
    ]
