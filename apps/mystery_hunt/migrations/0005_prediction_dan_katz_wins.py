# Generated by Django 2.0 on 2018-01-08 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mystery_hunt', '0004_auto_20180107_2241'),
    ]

    operations = [
        migrations.AddField(
            model_name='prediction',
            name='dan_katz_wins',
            field=models.BooleanField(default=False),
        ),
    ]
