# Generated by Django 4.2 on 2023-05-01 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_aviatickets_fly_start_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='aviatickets',
            name='number_tickets',
            field=models.IntegerField(null=True),
        ),
    ]