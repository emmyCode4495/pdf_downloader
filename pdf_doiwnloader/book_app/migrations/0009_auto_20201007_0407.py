# Generated by Django 3.1.1 on 2020-10-07 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0008_auto_20201007_0356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='edition',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='file_size',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='file_type',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
