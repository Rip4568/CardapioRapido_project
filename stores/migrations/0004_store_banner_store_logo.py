# Generated by Django 5.0.3 on 2024-03-10 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0003_store_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='banner',
            field=models.ImageField(blank=True, null=True, upload_to='stores/banners/', verbose_name='Banner da loja'),
        ),
        migrations.AddField(
            model_name='store',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='stores/logos/', verbose_name='Logo da loja'),
        ),
    ]
