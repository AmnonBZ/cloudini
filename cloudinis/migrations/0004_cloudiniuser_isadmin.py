# Generated by Django 3.0.4 on 2020-06-23 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cloudinis', '0003_auto_20200614_2012'),
    ]

    operations = [
        migrations.AddField(
            model_name='cloudiniuser',
            name='isAdmin',
            field=models.BooleanField(default=False),
        ),
    ]
