# Generated by Django 4.1.7 on 2023-11-14 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0030_cart_list_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='values',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
    ]
