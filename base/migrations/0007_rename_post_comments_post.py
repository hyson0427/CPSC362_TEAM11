# Generated by Django 4.1.2 on 2022-12-02 05:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_rename_post_comments_post_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='Post',
            new_name='post',
        ),
    ]
