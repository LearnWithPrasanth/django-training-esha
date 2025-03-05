from django import forms
from django.contrib.auth import get_user_model


class RegistrationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Confirm Password', widget=forms.PasswordInput
    )

    class Meta:
        model = get_user_model()
        fields = {'username', 'full_name', 'email', 'mobile'}
        widgets = {
            'full_name': forms.TextInput(attrs={'autofocus': True})
        }

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        phone = cleaned_data.get('mobile')
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if not email and not phone:
            raise forms.ValidationError(
                "Please provide an email or mobile number")

        if password1 != password2:
            raise forms.ValidationError("Passwords do not match")

        def save(self, commit=True):
            user = super().save(commit=False)
            if commit:
                user.save()
            return user
