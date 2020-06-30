# Generated by Django 3.0.7 on 2020-06-29 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0005_auto_20200629_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='ma_pod_setup',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=None, max_length=150),
        ),
        migrations.AlterField(
            model_name='request',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('In Process', 'In Process'), ('Completed', 'Completed'), ('Transferred', 'Transferred')], default=None, max_length=150),
        ),
    ]
