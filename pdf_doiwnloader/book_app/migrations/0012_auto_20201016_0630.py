# Generated by Django 3.1.1 on 2020-10-16 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0011_auto_20201012_1754'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='document',
            new_name='file_upload',
        ),
    ]