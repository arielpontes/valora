from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("estimates", "0002_update_inquiry_fields"),
    ]

    operations = [
        migrations.AddField(
            model_name="estimate",
            name="ten_year_revenue",
            field=models.JSONField(default=list),
        ),
        migrations.AddField(
            model_name="estimate",
            name="ten_year_cost",
            field=models.JSONField(default=list),
        ),
    ]
