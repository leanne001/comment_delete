# Generated by Django 2.2.1 on 2019-05-11 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_comment_password'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='password',
            new_name='dropdown',
        ),
    ]
