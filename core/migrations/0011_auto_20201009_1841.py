# Generated by Django 3.1.2 on 2020-10-09 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20201007_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statepoll',
            name='moe',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
