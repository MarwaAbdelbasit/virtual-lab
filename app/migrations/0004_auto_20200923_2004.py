# Generated by Django 3.1 on 2020-09-23 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_faq_reservation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='Answer',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
    ]