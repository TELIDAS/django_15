# Generated by Django 4.0.4 on 2022-04-18 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0003_tvshow_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tvshow',
            name='duration',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]