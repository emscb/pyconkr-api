# Generated by Django 2.2 on 2019-04-29 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0045_auto_20190429_1914'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticketproduct',
            name='ticket_total',
        ),
        migrations.AddField(
            model_name='ticketproduct',
            name='total',
            field=models.IntegerField(default=0, help_text='판매할 티켓의 총 개수입니다.'),
        ),
    ]
