# Generated by Django 4.0.2 on 2022-03-18 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_remove_comment_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]