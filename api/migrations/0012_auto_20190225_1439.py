# Generated by Django 2.1.5 on 2019-02-25 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20190223_1502'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sponsorlevel',
            name='desc',
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar_url',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]