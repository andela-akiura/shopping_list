from django import forms

class SignUpForm(forms.Form):
    username = forms.CharField(label='username', name='username',
                               id='username',
                               widget=forms.TextInput(
                                   attrs={'placeholder': 'Create username',
                                          'autocomplete': 'off'}))
    email = forms.CharField(label='Email', name='username',
                            id='username',
                            widget=forms.EmailInput(
                                attrs={'placeholder': 'Create username',
                                       'autocomplete': 'off'}))
    password = forms.CharField(label='Email', name='username',
                               id='username',
                               widget=forms.PasswordInput(
                                   attrs={'placeholder': 'Create password',
                                          'autocomplete': 'off'}))
