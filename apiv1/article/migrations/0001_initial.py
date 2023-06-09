# Generated by Django 4.1 on 2023-06-12 02:01

import article.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='comment1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fromu', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'comment1',
                'verbose_name_plural': 'comment1s',
                'db_table': 'comment1',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='comment2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fromu', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'comment2',
                'verbose_name_plural': 'comment2s',
                'db_table': 'comment2',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Nav1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'nav1',
                'verbose_name_plural': 'nav1s',
                'db_table': 'nav1',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Nav2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('nav1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.nav1', to_field='name')),
            ],
            options={
                'verbose_name': 'nav2',
                'verbose_name_plural': 'nav2s',
                'db_table': 'nav2',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('digest', models.TextField(max_length=128)),
                ('article_cover', models.ImageField(default='article/default/default.png', upload_to=article.models.article_img_path)),
                ('body', models.TextField()),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('upvote', models.PositiveIntegerField(default=0, help_text='点赞量')),
                ('collect', models.PositiveIntegerField(default=0, help_text='收藏量')),
                ('pageviews', models.PositiveIntegerField(default=0, help_text='阅读量')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
            options={
                'verbose_name': 'article',
                'verbose_name_plural': 'articles',
                'db_table': 'article',
                'ordering': ('id', 'author', 'date_create'),
            },
        ),
    ]
