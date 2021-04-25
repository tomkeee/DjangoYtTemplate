from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()

# non_allowed_usernames=["abc"]

class RegisterForm(forms.Form):
    username = forms.CharField()
    email=forms.EmailField(required=True)
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={"class": "form-control"}
        )
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(
        attrs={"class": "form-control",
              })
    )  
    def clean_username(self):
        username= self.cleaned_data.get("username")
        qs = User.objects.filter(username__iexact=username)
        # if username in non_allowed_usernames:
        #     raise forms.ValidationError("This is an invalid username")
        if qs.exists():
            raise forms.ValidationError("This user is not valid.")
        return username

    def clean_email(self):
        email= self.cleaned_data.get("email")
        qs = User.objects.filter(email__iexact=email)
        if qs.exists():
            raise forms.ValidationError("This email is already taken, please pick another.")
        return email

    def clean_password2(self):
        # cleaned_data = super(UserForm, self).clean()
        password = self.cleaned_data.get("password1")
        confirm_password = self.cleaned_data.get("password2")

        if password != confirm_password:
            raise forms.ValidationError(
                "given passwords do not match"
            )
        return password2



class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control",
                    "id":"user-password"
            }
        )
    )
    # def clean(self):
    #     username=self.cleaned_data.get("username")
    #     password=self.cleaned_data.get("password")

    def clean_username(self):
        username= self.cleaned_data.get("username")
        qs = User.objects.filter(username__iexact=username)
        # if username in non_allowed_usernames:
        #     raise forms.ValidationError("This is an invalid username")
        if not qs.exists():
            raise forms.ValidationError("This user does not exist.")
        return username
