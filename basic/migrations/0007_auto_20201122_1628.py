# Generated by Django 3.0.5 on 2020-11-22 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0006_product_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='responseType',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
