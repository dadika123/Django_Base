from django import forms

from authapp.forms import ShopUserRegisterForm, ShopUserProfileForm
from authapp.models import User
from mainapp.models import Product


class NewAdminRegisterForm(ShopUserRegisterForm):
    avatar = forms.ImageField(widget=forms.FileInput(), required=False)

    class Meta:
        model = User
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(NewAdminRegisterForm, self).__init__(*args, **kwargs)
        self.fields['avatar'].widget.attrs['class'] = 'custom-file-input'


class NewAdminProfileForm(ShopUserProfileForm):
    avatar = forms.ImageField(widget=forms.FileInput(), required=False)

    def __init__(self, *args, **kwargs):
        super(NewAdminProfileForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['readonly'] = False
        self.fields['email'].widget.attrs['readonly'] = False


class ProductCreateForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput())

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ProductCreateForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'image':
                field.widget.attrs['class'] = 'custom-file-input'
            else:
                field.widget.attrs['class'] = 'form-control py-4'
