# Generated by Django 2.1.4 on 2019-01-11 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flickrdb', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fphoto',
            old_name='group',
            new_name='groupid',
        ),
    ]
