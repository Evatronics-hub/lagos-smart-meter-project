from django import forms
from django.contrib.auth import get_user_model

class StaffForm(forms.ModelForm):
    name = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class' :'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class' :'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class' :'form-control'}))
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = get_user_model()
        fields = ('name', 'email')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = get_user_model().objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email is taken")
        return email

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password2"])
        user.staff = True
        if commit:
            user.save()
        return user