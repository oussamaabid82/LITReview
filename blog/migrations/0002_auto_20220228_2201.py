# Generated by Django 3.2 on 2022-02-28 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='contributors',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='contributors',
        ),
        migrations.DeleteModel(
            name='BlogContributor',
        ),
    ]
