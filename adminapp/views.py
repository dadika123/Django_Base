from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from adminapp.forms import NewAdminRegisterForm, NewAdminProfileForm, NewAdminProductCategoryForm
from authapp.models import User
from mainapp.models import ProductCategory


@user_passes_test(lambda u: u.is_superuser, login_url='/')
def index(request):
    return render(request, 'adminapp/admin.html')


class UserListView(ListView):
    model = User
    template_name = 'adminapp/admin-users-read.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser, login_url='/'))
    def dispatch(self, request, *args, **kwargs):
        return super(UserListView, self).dispatch(request, *args, **kwargs)


# @user_passes_test(lambda u: u.is_superuser, login_url='/')
# def admin_users(request):
#     context = {'users': ShopUser.objects.all()}
#     return render(request, 'adminapp/admin-users-read.html', context)


class UserCreateView(CreateView):
    model = User
    template_name = 'adminapp/admin-users-create.html'
    form_class = NewAdminRegisterForm
    success_url = reverse_lazy('new_admin:admin_users')


# @user_passes_test(lambda u: u.is_superuser, login_url='/')
# def admin_users_create(request):
#     if request.method == 'POST':
#         register_form = NewAdminRegisterForm(
#             data=request.POST, files=request.FILES)
#         if register_form.is_valid():
#             register_form.save()
#             return HttpResponseRedirect(reverse('new_admin:admin_users'))
#     else:
#         register_form = NewAdminRegisterForm()
#     context = {'register_form': register_form}
#     return render(request, 'adminapp/admin-users-create.html', context)


class UserUpdateView(UpdateView):
    model = User
    template_name = 'adminapp/admin-users-update-delete.html'
    form_class = NewAdminProfileForm
    success_url = reverse_lazy('new_admin:admin_users')

    def get_context_data(self, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Редактирование пользователя'
        return context


#
# @user_passes_test(lambda u: u.is_superuser, login_url='/')
# def admin_users_update(request, user_id):
#     user = User.objects.get(id=user_id)
#     if request.method == 'POST':
#         profile_form = NewAdminProfileForm(
#             data=request.POST, files=request.FILES, instance=user)
#         if profile_form.is_valid():
#             profile_form.save()
#             return HttpResponseRedirect(reverse('new_admin:admin_users'))
#     else:
#         profile_form = NewAdminProfileForm(instance=user)
#         context = {'profile_form': profile_form,
#                    'user': user, 'media_url': MEDIA_URL}
#         return render(request, 'adminapp/admin-users-update-delete.html', context)


class UserDeleteView(DeleteView):
    model = User
    template_name = 'adminapp/admin-users-update-delete.html'
    success_url = reverse_lazy('new_admin:admin_users')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


def admin_categories(request):
    context = {'categories': ProductCategory.objects.all()}
    return render(request, 'adminapp/categories_read.html', context)


def admin_category_create(request):
    if request.method == 'POST':
        category_form = NewAdminProductCategoryForm(data=request.POST)
        if category_form.is_valid():
            category_form.save()
            return HttpResponseRedirect(reverse('new_admin:admin_categories'))
    else:
        category_form = NewAdminProductCategoryForm()
    context = {'category_form': category_form}
    return render(request, 'adminapp/categories_create.html', context)
