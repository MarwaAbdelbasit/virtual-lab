# Generated by Django 3.1 on 2020-09-18 22:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Devices',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('device_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('status', models.BooleanField(default=True)),
                ('description', models.TextField()),
                ('rate', models.IntegerField()),
                ('review', models.TextField()),
                ('category', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, default='device_default.png', upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Experiments',
            fields=[
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('experiment_id', models.IntegerField(primary_key=True, serialize=False)),
                ('duration', models.DurationField()),
                ('device_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.devices')),
            ],
        ),
    ]
