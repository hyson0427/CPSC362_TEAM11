# Generated by Django 4.1.2 on 2022-12-02 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_rename_comment_comments_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='contact',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]
