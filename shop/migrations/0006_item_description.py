# Generated by Django 4.2.2 on 2023-07-05 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0005_alter_item_options_remove_item_user_item_category_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="description",
            field=models.TextField(null=True),
        ),
    ]
