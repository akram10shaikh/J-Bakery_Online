# Generated by Django 4.1.7 on 2023-11-14 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0029_cart_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart_list',
            name='img',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
