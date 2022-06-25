from django.db import models
from datetime import date
import django

# Create your models here.
class UserList(models.Model):
    id = models.AutoField(primary_key=True)
    studentid = models.CharField('学籍番号', max_length=5)
    username = models.CharField('ユーザー名', max_length=10)
    userpassword = models.CharField('パスワード', max_length=200) #後で考える

    def __str__(self):
        return self.studentid


class BookList(models.Model):
    id = models.AutoField(primary_key=True)
    studentid = models.ForeignKey(UserList, on_delete=models.CASCADE)
    title = models.CharField('本のタイトル', max_length=200)
    date = models.DateField('本を借りた日', default = django.utils.timezone.now)
# date.today()
    def __str__(self):
        return self.title
