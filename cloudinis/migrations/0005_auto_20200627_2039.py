# Generated by Django 3.0.4 on 2020-06-27 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cloudinis', '0004_cloudiniuser_isadmin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activatedpolicy',
            name='organization',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='cloudinis.Organization'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
