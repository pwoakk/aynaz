# Generated by Django 3.2.9 on 2022-05-07 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(default=None, null=True, upload_to='category_images/', verbose_name='Фото'),
        ),
    ]
