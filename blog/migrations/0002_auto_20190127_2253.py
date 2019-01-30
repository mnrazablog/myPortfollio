# Generated by Django 2.0.7 on 2019-01-27 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='desc',
        ),
        migrations.AddField(
            model_name='blog',
            name='body',
            field=models.TextField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='blog',
            name='pub_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(upload_to='blogsimage/'),
        ),
    ]
