# Generated by Django 3.0.2 on 2020-08-30 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('product_descp', models.CharField(max_length=300)),
                ('publish_date', models.DateField()),
            ],
        ),
    ]