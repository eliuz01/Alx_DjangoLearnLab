# Generated by Django 5.1.6 on 2025-03-02 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0004_alter_book_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': [('can_create', 'can create a bookshelf'), ('can_view', 'can view a bookshelf'), ('can_edit', 'can edit a bookshelf'), ('can_delete', 'can delete a bookshelf')]},
        ),
    ]
