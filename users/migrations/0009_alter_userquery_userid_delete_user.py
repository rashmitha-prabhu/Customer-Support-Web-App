# Generated by Django 4.1.2 on 2022-10-30 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_rename_users_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userquery',
            name='userID',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
