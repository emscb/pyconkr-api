# Generated by Django 2.2 on 2019-04-12 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0030_auto_20190412_2336'),
    ]

    operations = [
        migrations.AddField(
            model_name='pyconkorea',
            name='babycare_ticket_finish_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pyconkorea',
            name='babycare_ticket_start_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pyconkorea',
            name='youngcoder_ticket_finish_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pyconkorea',
            name='youngcoder_ticket_start_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
