# Generated by Django 3.0.2 on 2020-10-31 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_remove_order_address_line2'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='itemsJson',
            field=models.CharField(default=2, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.IntegerField(default=0),
        ),
    ]
