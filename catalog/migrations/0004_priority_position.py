# Generated by Django 2.2.3 on 2019-08-01 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20190801_1812'),
    ]

    operations = [
        migrations.AddField(
            model_name='priority',
            name='position',
            field=models.IntegerField(default=0),
        ),
    ]
