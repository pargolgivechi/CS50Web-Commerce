# Generated by Django 4.0.2 on 2022-03-30 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0018_bid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='bid_price',
            field=models.FloatField(default=0),
        ),
    ]
