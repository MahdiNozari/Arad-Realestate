# Generated by Django 5.1.2 on 2024-12-09 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_file_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='price',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
