# Generated by Django 4.1.2 on 2022-12-08 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_post_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='username',
            field=models.CharField(default='anonim', max_length=255),
        ),
    ]
