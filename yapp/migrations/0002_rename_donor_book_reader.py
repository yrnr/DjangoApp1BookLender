# Generated by Django 4.0 on 2021-12-10 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='donor',
            new_name='reader',
        ),
    ]
