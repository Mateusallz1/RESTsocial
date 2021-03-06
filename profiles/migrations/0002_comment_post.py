# Generated by Django 3.0 on 2020-12-21 01:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.CharField(max_length=500)),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post', to='profiles.Profile')),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.CharField(max_length=500)),
                ('postid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='profiles.Post')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
