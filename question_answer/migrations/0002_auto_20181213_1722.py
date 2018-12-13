# Generated by Django 2.1.2 on 2018-12-13 09:22

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question_answer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='describe',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='blocked_users',
            field=models.ManyToManyField(related_name='_user_blocked_users_+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user',
            name='followed_answers',
            field=models.ManyToManyField(related_name='followed_answers', to='question_answer.Answer'),
        ),
        migrations.AlterField(
            model_name='user',
            name='followed_questions',
            field=models.ManyToManyField(related_name='followed_questions', to='question_answer.Question'),
        ),
        migrations.AlterField(
            model_name='user',
            name='followed_users',
            field=models.ManyToManyField(related_name='_user_followed_users_+', to=settings.AUTH_USER_MODEL),
        ),
    ]
