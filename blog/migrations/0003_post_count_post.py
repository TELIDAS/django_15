# Generated by Django 4.0.4 on 2022-05-16 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='count_post',
            field=models.IntegerField(null=True),
        ),
    ]
