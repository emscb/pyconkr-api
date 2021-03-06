# Generated by Django 2.1.5 on 2019-04-06 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20190406_1929'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsorlevel',
            name='booth_size',
            field=models.IntegerField(default=0, help_text='후원사에게 제공되는 부스 크기'),
        ),
        migrations.AddField(
            model_name='sponsorlevel',
            name='can_provide_goods',
            field=models.BooleanField(default=False, help_text='후원사 증정품을 파이콘 참가자에게 제공할 수 있는지 여부'),
        ),
        migrations.AddField(
            model_name='sponsorlevel',
            name='can_recruit',
            field=models.BooleanField(default=True, help_text='후원사 채용 공고를 할 수 있는지 여부'),
        ),
        migrations.AddField(
            model_name='sponsorlevel',
            name='logo_locations',
            field=models.TextField(blank=True, help_text='로고가 노출되는 위치에 대한 설명입니다.', null=True),
        ),
        migrations.AddField(
            model_name='sponsorlevel',
            name='ost_room_info',
            field=models.CharField(blank=True, help_text='후원사에게 제공되는 OST 룸 정보', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='sponsorlevel',
            name='program_guide',
            field=models.CharField(blank=True, help_text='프로그램 가이드에 후원사 소개가 수록되는 것에 대한 정보', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='sponsorlevel',
            name='limit',
            field=models.IntegerField(default=0, help_text='후원사 등급 별 구좌수'),
        ),
        migrations.AlterField(
            model_name='sponsorlevel',
            name='presentation_count',
            field=models.IntegerField(default=0, help_text='후원사에게 제공되는 스폰서 발표 수'),
        ),
        migrations.AlterField(
            model_name='sponsorlevel',
            name='ticket_count',
            field=models.IntegerField(default=0, help_text='후원사에게 제공되는 티켓 수'),
        ),
    ]
