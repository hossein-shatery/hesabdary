# Generated by Django 4.2.4 on 2023-09-11 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kh_d', '0004_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='token',
            field=models.CharField(max_length=25),
        ),
    ]
