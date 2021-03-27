from django import forms

from authapp.forms import ShopUserRegisterForm, ShopUserProfileForm
from authapp.models import User


class NewAdminRegisterForm(ShopUserRegisterForm):
    avatar = forms.ImageField(widget=forms.FileInput(), required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'avatar', 'first_name', 'last_name', 'age', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(NewAdminRegisterForm, self).__init__(*args, **kwargs)
        self.fields['avatar'].widget.attrs['class'] = 'custom-file-input'


class NewAdminProfileForm(ShopUserProfileForm):
    avatar = forms.ImageField(widget=forms.FileInput(), required=False)

    def __init__(self, *args, **kwargs):
        super(NewAdminProfileForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['readonly'] = False
        self.fields['email'].widget.attrs['readonly'] = False
