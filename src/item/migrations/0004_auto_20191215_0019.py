# Generated by Django 2.2.7 on 2019-12-14 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0003_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.FileField(blank=True, default='../static/item/img/default_item_image.png', upload_to='img/'),
        ),
    ]
