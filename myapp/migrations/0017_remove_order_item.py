# Generated by Django 4.1.7 on 2023-11-09 05:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_alter_order_order_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='item',
        ),
    ]
