# Generated by Django 2.1.2 on 2018-12-13 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question_answer', '0002_auto_20181213_1722'),
    ]

    operations = [
        migrations.AddField(
            model_name='blocklist',
            name='reason',
            field=models.TextField(default=''),
        ),
    ]
