# Generated by Django 4.2 on 2023-04-09 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickets',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]