# Generated by Django 3.0.5 on 2020-11-22 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0008_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
