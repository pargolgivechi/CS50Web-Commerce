# Generated by Django 4.0.2 on 2022-03-14 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(choices=[('Electronic', 'Electronic'), ('Furniture', 'Furniture'), ('Toy', 'Toy'), ('Clothing', 'Clothing'), ('Kitchen', 'Kitchen')], default='Electronic', max_length=20),
        ),
    ]
