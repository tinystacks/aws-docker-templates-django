# Generated by Django 2.0 on 2021-08-18 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0007_auto_20210817_2203'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.AlterField(
            model_name='todolist',
            name='created',
            field=models.DateField(default='2021-08-18'),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='due_date',
            field=models.DateField(default='2021-08-18'),
        ),
    ]
