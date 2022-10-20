# Generated by Django 4.0.2 on 2022-03-14 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_alter_category_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(choices=[('Electronic', 'Electronic'), ('Furniture', 'Furniture'), ('Toy', 'Toy'), ('Clothing', 'Clothing'), ('Kitchen', 'Kitchen')], default='Toy', max_length=20),
        ),
    ]
