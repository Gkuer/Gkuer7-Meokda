from django import forms
from .models import meokda_user
from django.contrib.auth.hashers import check_password
from django.forms import ModelForm

class LoginForm(forms.Form):
    username = forms.CharField(
        error_messages={
            'required': '아이디를 입력해주세요'
        },
        max_length = 32, label = "사용자 이름")
    password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력해주세요'
        },
        widget = forms.PasswordInput, label = "비밀번호")

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password :
            try:
                meokdauser = meokda_user.objects.get(username = username)
            except meokda_user.DoesNotExist:
                self.add_error('username', '아이디가 없습니다.')
                return
            if not check_password(password, meokdauser.password):
                self.add_error('password', '비밀번호를 틀렸습니다.')
            else:
                self.username = meokdauser.username

class ImageForm(ModelForm):
    class Meta:
        model = meokda_user
        fields = '__all__'
        exclude = ['username', 'useremail','password']