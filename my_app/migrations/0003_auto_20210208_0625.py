# Generated by Django 3.1.5 on 2021-02-08 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_auto_20210202_0143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search',
            name='search',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
