# Generated by Django 4.1.2 on 2022-12-13 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_comment_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='username',
            field=models.CharField(max_length=255),
        ),
    ]
