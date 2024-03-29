# Generated by Django 2.2.19 on 2022-11-04 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Group name')),
                ('slug', models.SlugField(unique=True, verbose_name='Group tag')),
                ('description', models.TextField(verbose_name='Group description')),
            ],
        ),
    ]
