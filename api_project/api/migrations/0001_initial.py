# Generated by Django 5.1.6 on 2025-03-04 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titie', models.CharField(max_length=200, verbose_name='Title')),
                ('author', models.CharField(max_length=100, verbose_name='Author')),
                ('published_date', models.DateField(verbose_name='Published Date')),
            ],
        ),
    ]
