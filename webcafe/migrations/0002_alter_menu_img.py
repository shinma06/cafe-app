# Generated by Django 4.0.6 on 2022-08-03 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webcafe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='メニュー画像'),
        ),
    ]
