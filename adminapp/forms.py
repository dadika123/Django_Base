from django import forms
from django.forms import ModelForm

from authapp.forms import ShopUserRegisterForm, ShopUserProfileForm
from authapp.models import ShopUser
from mainapp.models import ProductCategory


class NewAdminRegisterForm(ShopUserRegisterForm):
    avatar = forms.ImageField(widget=forms.FileInput(), required=False)

    class Meta:
        model = ShopUser
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


class NewAdminProductCategoryForm(ModelForm):
    class Meta:
        model = ProductCategory
        fields = ('name', 'description',)

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
        self.fields['description'].widget.attrs['rows'] = 2
