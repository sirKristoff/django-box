# Generated by Django 2.2.8 on 2019-12-17 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0004_auto_20191215_0019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, default='../static/item/img/default_item_image.png', upload_to='img/'),
        ),
    ]
