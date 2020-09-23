# Generated by Django 3.1 on 2020-09-23 12:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200921_0133'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('Question', models.CharField(max_length=100)),
                ('Answer', models.CharField(max_length=10, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Start_time', models.DateTimeField()),
                ('Finish_time', models.DateTimeField()),
                ('Device', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='app.devices')),
                ('user', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
