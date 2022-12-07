from django.urls import path

from .views import BlogLoginView, BlogLogoutView, InfoLogoutView, UserDetailView, UserUpdateView, SignUpView

app_name = 'login'
urlpatterns = [
    path('', BlogLoginView.as_view(), name='login'),
    path('logout/', BlogLogoutView.as_view(), name='logout'),
    path('logout/info', InfoLogoutView.as_view(), name='logout_info'),
    path('userdetail', UserDetailView.as_view(), name='user_detail'),
    path('userupdate/', UserUpdateView.as_view(), name='user_update'),
    path('signup/', SignUpView.as_view(), name='signup'),

]
