# Generated by Django 3.0.7 on 2020-06-29 20:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0002_auto_20200629_0157'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
