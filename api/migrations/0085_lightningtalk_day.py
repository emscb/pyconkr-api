# Generated by Django 2.2 on 2019-08-13 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0084_auto_20190813_1620'),
    ]

    operations = [
        migrations.AddField(
            model_name='lightningtalk',
            name='day',
            field=models.IntegerField(default=1),
        ),
    ]
