# Generated by Django 5.0.3 on 2024-03-10 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0004_store_banner_store_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created at'),
        ),
    ]
