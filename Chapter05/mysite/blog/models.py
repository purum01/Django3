from django.db import models

class Post(models.Model):
    REGION_CHOICE = (
                        ('Africa','아프리카'),
                        ('Europe','유럽'),
                        ('Oceania','오세아니아'),
                        ('Asia','아시아'),
                        ('North America','북아메리카'),
                        ('South America','남아메리카'),
                    )

    title = models.CharField('제목', max_length=250)
    body = models.TextField('내용')
    region = models.CharField('지역',max_length=20,choices=REGION_CHOICE, default='Asia')
    tag = models.ManyToManyField('Tag')
    created = models.DateField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title   


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.CharField(max_length=20)
    message = models.TextField()
    created = models.DateField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True)

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name 