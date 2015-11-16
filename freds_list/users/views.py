from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.models import User
from users.forms import UserCreateForm
from django.views.generic import CreateView


class CreateUser(CreateView):

    model = User
    form_class = UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'users/register.html'


