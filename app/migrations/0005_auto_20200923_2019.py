# Generated by Django 3.1 on 2020-09-23 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20200923_2004'),
    ]

    operations = [
        migrations.AddField(
            model_name='faq',
            name='question_id',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='faq',
            name='Answer',
            field=models.CharField(max_length=255),
        ),
    ]
