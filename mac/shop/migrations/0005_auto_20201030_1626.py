# Generated by Django 3.0.2 on 2020-10-30 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='zip',
            new_name='zip_code',
        ),
    ]
