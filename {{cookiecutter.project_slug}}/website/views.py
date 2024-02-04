from django.views import View
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from website.forms import SignupForm


class WebsiteView(View):
    def get(self, request):
        return render(request, "website/home.html")


class RegisterView(View):
    def get(self, request):
        form = SignupForm()
        return render(request, "website/register.html", {"form": form})

    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()

            password = form.cleaned_data.get("password1")
            auth_user = authenticate(username=user.username, password=password)
            if auth_user is not None:
                login(request, auth_user)
                return redirect("/dashboard")
            else:
                user.delete()
                messages.error(
                    request,
                    "Houve um erro ao tentar criar o usuário. Por favor, tente novamente.",
                )
                return render(request, "website/register.html", {"form": form})
        return render(request, "website/register.html", {"form": form})


class DashboardView(View):
    def get(self, request):
        if request.user.is_authenticated and request.user.tenant_id:
            return render(request, "website/dashboard.html")

        return render(request, "website/dashboard.html")
