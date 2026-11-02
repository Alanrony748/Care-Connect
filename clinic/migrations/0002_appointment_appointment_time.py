import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("clinic", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="appointment",
            name="appointment_time",
            field=models.TimeField(default=datetime.time(0, 0)),
            preserve_default=False,
        ),
    ]
