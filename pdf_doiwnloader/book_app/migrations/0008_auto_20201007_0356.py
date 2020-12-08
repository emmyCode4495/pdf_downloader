# Generated by Django 3.1.1 on 2020-10-07 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0007_auto_20201006_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='edition',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='file_size',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='file_type',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
    ]