# Generated by Django 4.1.5 on 2023-01-20 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_book_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='price',
            new_name='pric',
        ),
    ]
