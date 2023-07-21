from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import View

from registration.forms import RegistrationForm
from tracker.models import CustomUser


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
