# Generated by Django 4.1.7 on 2023-11-09 05:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0020_orderstatus_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_status',
        ),
    ]
