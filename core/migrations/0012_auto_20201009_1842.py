# Generated by Django 3.1.2 on 2020-10-09 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20201009_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statepoll',
            name='n',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
