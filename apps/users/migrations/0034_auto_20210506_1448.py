# Generated by Django 3.1 on 2021-05-06 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0033_user_need_update_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='dingtalk_id',
            field=models.CharField(default=None, max_length=128, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='user',
            name='wecom_id',
            field=models.CharField(default=None, max_length=128, null=True, unique=True),
        ),
    ]