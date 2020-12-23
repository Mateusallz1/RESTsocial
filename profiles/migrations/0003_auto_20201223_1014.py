# Generated by Django 3.0 on 2020-12-23 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_comment_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='postid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='profiles.Post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='userid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='profiles.Profile'),
        ),
    ]
