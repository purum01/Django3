from django.db import models
from django.conf import settings

class User(models.Model):
    username = models.CharField('계정',
                                max_length=150,
                                unique=True,
                                help_text='필수. 150자 이하. 문자, 숫자 및 @ /. /+ /- /_ 만 사용',
                                error_messages={
                                    'unique': "존재하는 계정입니다",
                                },
                            )
    password = models.CharField('비밀번호', max_length=128)
    name = models.CharField('이름', max_length=150, blank=True)
    email = models.EmailField('이메일', blank=True)
    is_active = models.BooleanField(default=True, help_text='계정을 삭제하는 대신 선택을 해제함')
    date_joined = models.DateTimeField('가입일자', auto_now_add=True)

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=50)


class Profile2(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    def __str__(self):
        return self.user.username
