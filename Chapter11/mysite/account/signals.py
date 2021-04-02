from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.mail import send_mail

@receiver(post_save, sender=User)
def welcome_send_mail(sender,**kwargs):
    if kwargs['created']:
        user = kwargs['instance']
        subject = 'welcome'
        message = f'{user.first_name}님 회원 가입을 축하드립니다!'
        send_mail(subject, message, 'admin@mysite.com', [user.email], fail_silently=False)
        
