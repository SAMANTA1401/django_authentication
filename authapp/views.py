from django.shortcuts import render,HttpResponse, render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView,FormView,TemplateView
from django.urls import reverse_lazy
from rootapp.forms import RegistrationFormSeller2 , RegistrationForm


# Create your views here.
# Create your views here.
def index(request):
    return render(request, 'authapp/index.html')


class LoginViewUser(LoginView):
    template_name = 'authapp/login.html'  # specify the login page to be used by``LoginView``
    # success_url = reverse_lazy('index')  # specify the URL to redirect to after successful login
    

class RegisterViewSeller(LoginRequiredMixin, CreateView):
    template_name = 'authapp/signup_seller.html'
    form_class = RegistrationFormSeller2
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = self.request.user
        user.type.append(user.Types.SELLER)
        user.save()
        form.instance.user = self.request.user
        return super().form_valid(form)


class RegisterView(CreateView):
    template_name = 'authapp/signup_user.html'
    form_class = RegistrationForm
    # success_url = reverse_lazy('index') ## this is for rootapp template
    success_url = reverse_lazy('authapp/index')




