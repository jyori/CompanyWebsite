# Generated by Django 2.1.7 on 2019-06-10 05:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cpost',
            old_name='contenttitle',
            new_name='ContentTitle',
        ),
    ]