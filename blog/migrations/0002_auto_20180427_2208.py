# Generated by Django 2.0.1 on 2018-04-28 03:08

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogindexpage',
            name='intro',
            field=wagtail.core.fields.RichTextField(),
        ),
    ]