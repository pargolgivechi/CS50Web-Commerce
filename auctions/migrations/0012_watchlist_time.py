# Generated by Django 4.0.2 on 2022-03-20 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_watchlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
