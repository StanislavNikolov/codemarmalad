from django.core.exceptions import ValidationError
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from django.db import IntegrityError

from accounts.models import User


class RegisterForm(forms.Form):
    email = forms.EmailField(label="Email")
    username = forms.CharField(
        label="Username",
        required=True,
        min_length=4
    )
    password1 = forms.CharField(
        label="Password",
        required=True,
        strip=False,
        min_length=6,
        widget=forms.PasswordInput(
            attrs={'placeholder': '******'}
        )
    )
    password2 = forms.CharField(
        label="Enter password again",
        required=True,
        strip=False,
        widget=forms.PasswordInput(
            attrs={'placeholder': '******'}
        )
    )

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                "Passwords do not match",
                code='password_mismatch',
            )
        return password2


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            try:
                user = User.objects.create_user(
                    username=form.cleaned_data.get('username'),
                    email=form.cleaned_data.get('email'),
                    password=form.cleaned_data.get('password1')
                )
            except IntegrityError as err:
                known_errors = {
                    'UNIQUE constraint failed: accounts_user.username': ('username', 'Username already exists!'),
                    'UNIQUE constraint failed: accounts_user.email': ('email', 'Email already exists!'),
                }
                internal_err = str(err)

                if internal_err not in known_errors:
                    print(internal_err)
                    form.add_error(None, 'Unknown error')
                else:
                    form.add_error(*known_errors[internal_err])

            if form.is_valid():
                user.save()
                login(request, user)
                return redirect('home')
    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


def user_view(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'accounts/user.html', {'user': user})
