# Generated by Django 3.2 on 2022-02-23 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20220223_1947'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='title',
            new_name='title_review',
        ),
    ]
