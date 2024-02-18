# Generated by Django 5.0.2 on 2024-02-13 03:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0001_initial'),
        ('orders', '0002_rename_date_order_startdate'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='client',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='order',
            name='house',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='houses.house'),
        ),
    ]