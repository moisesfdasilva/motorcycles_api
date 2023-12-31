# Generated by Django 4.2.4 on 2023-08-02 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motorcycles_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manufacturer',
            name='added_by',
        ),
        migrations.RemoveField(
            model_name='motorcycle',
            name='added_by',
        ),
        migrations.AddField(
            model_name='manufacturer',
            name='founded',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='motorcycle',
            name='engine_cc',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='motorcycle',
            name='year',
            field=models.IntegerField(null=True),
        ),
    ]
