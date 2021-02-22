# Generated by Django 3.1.4 on 2020-12-22 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(error_messages={'unique': '존재하는 계정입니다'}, help_text='필수. 150자 이하. 문자, 숫자 및 @ /. / + /-/ _ 만 사용', max_length=150, unique=True, verbose_name='계정')),
                ('password', models.CharField(max_length=128, verbose_name='비밀번호')),
                ('name', models.CharField(blank=True, max_length=150, verbose_name='이름')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='이메일')),
                ('is_active', models.BooleanField(default=True, help_text='계정을 삭제하는 대신 선택을 해제함')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='가입일자')),
            ],
        ),
    ]