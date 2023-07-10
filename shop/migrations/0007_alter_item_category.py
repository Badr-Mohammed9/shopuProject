# Generated by Django 4.2.2 on 2023-07-09 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0006_item_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="category",
            field=models.CharField(
                choices=[
                    ("Electronics", "Electronics"),
                    ("Fashion", "Fashion"),
                    ("Sports and Outdoors", "Sports and Outdoors"),
                    ("Toys and Games", "Toys and Games"),
                ],
                default="Uncategorized",
                max_length=50,
            ),
        ),
    ]
