# Generated by Django 2.0.1 on 2018-03-02 02:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_owner_organization_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='owner',
            old_name='organization_id',
            new_name='organization',
        ),
        migrations.RenameField(
            model_name='owner',
            old_name='user_id',
            new_name='user',
        ),
    ]