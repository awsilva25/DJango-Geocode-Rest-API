# Generated by Django 3.0 on 2020-02-20 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='distance',
            name='dest_lat',
            field=models.DecimalField(decimal_places=20, default=None, max_digits=30),
        ),
        migrations.AddField(
            model_name='distance',
            name='dest_long',
            field=models.DecimalField(decimal_places=20, default=None, max_digits=30),
        ),
        migrations.AddField(
            model_name='distance',
            name='full_dest_address',
            field=models.CharField(default=None, max_length=250),
        ),
        migrations.AddField(
            model_name='distance',
            name='full_origin_address',
            field=models.CharField(default=None, max_length=250),
        ),
        migrations.AddField(
            model_name='distance',
            name='origin_lat',
            field=models.DecimalField(decimal_places=20, default=None, max_digits=30),
        ),
        migrations.AddField(
            model_name='distance',
            name='origin_long',
            field=models.DecimalField(decimal_places=20, default=None, max_digits=30),
        ),
        migrations.AlterField(
            model_name='distance',
            name='destination',
            field=models.CharField(default=None, max_length=250),
        ),
        migrations.AlterField(
            model_name='distance',
            name='origin',
            field=models.CharField(default=None, max_length=250),
        ),
    ]