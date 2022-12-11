from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views import generic

from .forms import UserForm, SignUpForm


class BlogLoginView(LoginView):
    template_name = 'login/login.html'
    redirect_authenticated_user = True


class BlogLogoutView(LogoutView):
    next_page = 'login:logout_info'


class InfoLogoutView(generic.TemplateView):
    template_name = 'login/logout.html'


class UserDetailView(generic.DetailView):
    model = User
    template_name = 'login/user_detail.html'

    # def get_object(self):
    #     return self.request.user


class UserUpdateView(generic.UpdateView):
    model = User
    template_name = 'login/user_update.html'
    form_class = UserForm
    success_url = 'login:user_detail'

    def get_object(self):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy('login:user_detail', kwargs={'pk': self.object.pk})


class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'login/user_update.html'
    success_url = reverse_lazy('login:login')

