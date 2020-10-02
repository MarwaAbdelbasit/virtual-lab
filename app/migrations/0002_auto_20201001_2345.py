# Generated by Django 3.1 on 2020-10-01 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='plan_name',
            field=models.CharField(choices=[('S', 'Standard'), ('P', 'Plus'), ('M', 'Premium')], default='S', max_length=1),
        ),
    ]