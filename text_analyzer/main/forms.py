from django.forms import Form, CharField
from django.core.exceptions import ValidationError


class RegisterForm(Form):
    username = CharField(max_length=150)
    password1 = CharField()
    password2 = CharField()

    def clean(self):
        data = super(RegisterForm, self).clean()
        if data["password1"] != data["password2"]:
            raise ValidationError("Passwords not same")
        return data
