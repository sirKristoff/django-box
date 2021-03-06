# Generated by Django 2.2.8 on 2019-12-27 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0005_auto_20191217_1742'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['id', '-name']},
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, default='/static/item/img/default_item_image.png', upload_to='img/'),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=120, unique=True),
        ),
    ]
