# Generated by Django 5.1.2 on 2024-11-06 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oshpaz', '0002_category_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.FileField(default='1', upload_to=''),
            preserve_default=False,
        ),
    ]
