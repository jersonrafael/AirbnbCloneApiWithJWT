# Generated by Django 5.0.2 on 2024-02-13 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_order_client_alter_order_house'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='endDate',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='startDate',
            field=models.DateField(null=True),
        ),
    ]
