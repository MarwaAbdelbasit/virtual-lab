# Generated by Django 3.1 on 2020-10-14 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20201002_0212'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]
