# Generated by Django 2.1.5 on 2019-02-17 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20190217_1131'),
    ]

    operations = [
        migrations.CreateModel(
            name='OAuthSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('github_client_id', models.CharField(blank=True, max_length=100, null=True)),
                ('github_client_secret', models.CharField(blank=True, max_length=100, null=True)),
                ('google_client_id', models.CharField(blank=True, max_length=100, null=True)),
                ('google_client_secret', models.CharField(blank=True, max_length=100, null=True)),
                ('facebook_client_id', models.CharField(blank=True, max_length=100, null=True)),
                ('facebook_client_secret', models.CharField(blank=True, max_length=100, null=True)),
                ('naver_client_id', models.CharField(blank=True, max_length=100, null=True)),
                ('naver_client_secret', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]