from django import forms
from .models import BookList
from django.contrib.auth.forms import AuthenticationForm

class BookListCreateForm(forms.ModelForm):
    class Meta:
        model = BookList
        fields = ('title', 'date', 'studentid')
        labels = {"title":"本のタイトル", "date":"貸出日", "studentid":"ユーザー名"}

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'     #　※１
            field.widget.attrs['placeholder'] = field.label  #  ※２

        #※１：全てのフォームの部品のclass属性に「form-control」を指定（bootstrapのフォームデザインを利用するため）
        #※２：全てのフォームの部品にpaceholderを定義して、入力フォームにフォーム名が表示されるように指定。