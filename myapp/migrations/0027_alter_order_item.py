# Generated by Django 4.1.7 on 2023-11-09 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0026_values_remove_order_item_order_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='item',
            field=models.ManyToManyField(to='myapp.values'),
        ),
    ]
