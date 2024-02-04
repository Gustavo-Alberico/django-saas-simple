from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User


class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        for fieldname in ["email", "password1", "password2"]:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs["class"] = "form-control"

    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        user.username = user.email
        if commit:
            user.save()
        return user
