from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Client, Peddler, Established
from django.contrib.admin import widgets


class ClientCreateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(ClientCreateForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['first_name'].widget.attrs.update({'autofocus': 'autofocus'})

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def save(self, commit=True):
        if not commit:
            raise NotImplementedError("Can't create User and Profile without database save")
        user = super(ClientCreateForm, self).save(commit=True)
        profile = Client(user=user)
        profile.save()
        return user, profile


class PeddlerCreateForm(UserCreationForm):
    cash = forms.BooleanField(initial=True, required=False)
    credit = forms.BooleanField(initial=False, required=False)
    debit = forms.BooleanField(initial=False, required=False)
    social = forms.BooleanField(initial=False, required=False)

    def __init__(self, *args, **kwargs):
        super(PeddlerCreateForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['first_name'].widget.attrs.update({'autofocus': 'autofocus'})
        self.fields['cash'].widget.attrs.update({'class': 'filled-in'})
        self.fields['credit'].widget.attrs.update({'class': 'filled-in'})
        self.fields['debit'].widget.attrs.update({'class': 'filled-in'})
        self.fields['social'].widget.attrs.update({'class': 'filled-in'})

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def save(self, commit=True):
        if not commit:
            raise NotImplementedError("Can't create User and Profile without database save")
        user = super(PeddlerCreateForm, self).save(commit=True)
        profile = Peddler(user=user, cash=self.cleaned_data['cash'], credit=self.cleaned_data['credit'],
                          debit=self.cleaned_data['debit'], social=self.cleaned_data['social'])
        profile.save()
        return user, profile


class EstablishedCreateForm(UserCreationForm):
    cash = forms.BooleanField(initial=True, required=False)
    credit = forms.BooleanField(initial=False, required=False)
    debit = forms.BooleanField(initial=False, required=False)
    social = forms.BooleanField(initial=False, required=False)
    start = forms.TimeField()
    end = forms.TimeField()

    def __init__(self, *args, **kwargs):
        super(EstablishedCreateForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['first_name'].widget.attrs.update({'autofocus': 'autofocus'})
        self.fields['cash'].widget.attrs.update({'class': 'filled-in'})
        self.fields['credit'].widget.attrs.update({'class': 'filled-in'})
        self.fields['debit'].widget.attrs.update({'class': 'filled-in'})
        self.fields['social'].widget.attrs.update({'class': 'filled-in'})

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def save(self, commit=True):
        if not commit:
            raise NotImplementedError("Can't create User and Profile without database save")
        user = super(EstablishedCreateForm, self).save(commit=True)
        profile = Established(user=user, cash=self.cleaned_data['cash'], credit=self.cleaned_data['credit'],
                              debit=self.cleaned_data['debit'], social=self.cleaned_data['social'],
                              start=self.cleaned_data['start'], end=self.cleaned_data['end'], )
        profile.save()
        return user, profile


class UpdateProfile(forms.ModelForm):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

    def clean_email(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')

        if email and User.objects.filter(email=email).exclude(username=username).count():
            raise forms.ValidationError('This email address is already in use. Please supply a different email address.')
        return email

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user