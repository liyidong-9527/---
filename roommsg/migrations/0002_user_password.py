# Generated by Django 3.0.3 on 2020-05-08 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roommsg', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_password',
            fields=[
                ('user', models.CharField(help_text='账户', max_length=20, primary_key=True, serialize=False, unique=True)),
                ('password', models.CharField(help_text='密码', max_length=200, unique=True)),
            ],
        ),
    ]
