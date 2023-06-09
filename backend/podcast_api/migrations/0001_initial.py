# Generated by Django 4.2 on 2023-04-17 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Podcast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(default='')),
                ('source', models.CharField(default='', max_length=255)),
                ('audio', models.CharField(default='', max_length=255)),
                ('image', models.CharField(default='', max_length=255)),
                ('episode_title', models.CharField(default='', max_length=255)),
                ('numLikes', models.IntegerField(default=0)),
                ('numDislikes', models.IntegerField(default=0)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
