from django import forms

class register (forms.Form):
    username = forms.CharField(label="Tài Khoản",max_length=30)
    pasword = forms.CharField(label="Mật khẩu", widget=forms.PasswordInput())
