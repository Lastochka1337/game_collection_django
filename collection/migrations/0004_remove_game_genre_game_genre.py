# Generated by Django 5.0.6 on 2024-06-08 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0003_genre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='genre',
        ),
        migrations.AddField(
            model_name='game',
            name='genre',
            field=models.ManyToManyField(to='collection.genre'),
        ),
    ]
