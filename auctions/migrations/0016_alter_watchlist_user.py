# Generated by Django 4.0.2 on 2022-03-21 14:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0015_watchlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlist',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
