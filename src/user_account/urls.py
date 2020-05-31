from django.urls import path
from django.views.generic import TemplateView

from user_account.views import CreateUserAccountView

urlpatterns = [
    path('register/success', TemplateView.as_view(template_name='success.html'), name='success'),
    path('register/', CreateUserAccountView.as_view(), name='registration'),

]