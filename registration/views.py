from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import View

from registration.forms import RegistrationForm, LoginForm


def landing(request):
    return HttpResponse('<h1>Hello world</h1>')


class RegistrationView(View):
    form_class = RegistrationForm
    template_name = 'registration/registration.html'

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_user = form.data
            form.save()

            print(new_user)
            return redirect('landing')
        return render(request, self.template_name, {"form": form})


class LoginView(View):
    form_class = LoginForm
    template_name = 'registration/login.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('landing')

        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, f'Hi {username.title()}, welcome back!')
                return HttpResponse('<h1>logged</h1>')

        messages.error(request, f'Invalid username or password')
        return render(request, self.template_name, {'form': self.form_class})



