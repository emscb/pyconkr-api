# Generated by Django 2.1.5 on 2019-02-25 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20190225_1439'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsorlevel',
            name='name_en',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='sponsorlevel',
            name='name_ko',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]