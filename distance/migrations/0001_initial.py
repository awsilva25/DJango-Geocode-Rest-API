# Generated by Django 3.0.3 on 2020-02-20 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Distance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin', models.CharField(max_length=250)),
                ('destination', models.CharField(max_length=250)),
            ],
        ),
    ]
