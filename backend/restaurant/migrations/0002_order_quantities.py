# Generated by Django 4.1.5 on 2023-02-06 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='quantities',
            field=models.TextField(default=dict),
        ),
    ]