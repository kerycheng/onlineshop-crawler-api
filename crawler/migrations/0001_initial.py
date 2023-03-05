# Generated by Django 4.1.7 on 2023-03-01 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='keyword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'keyword',
            },
        ),
        migrations.CreateModel(
            name='momoshop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('brand', models.CharField(max_length=50)),
                ('link', models.URLField()),
                ('price', models.CharField(blank=True, max_length=50)),
                ('amount', models.CharField(max_length=50)),
                ('cate', models.CharField(max_length=200)),
                ('desc', models.TextField(blank=True, max_length=1000)),
            ],
            options={
                'db_table': 'momoshop',
            },
        ),
    ]
