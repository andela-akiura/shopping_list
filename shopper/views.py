from django.shortcuts import render
from django.views import generic
from forms import SignUpForm
# Create your views here.

class ShopperSignUpView(generic.TemplateView):
    form_class = SignUpForm
    template_name = 'signup.html'

    def post(self, request, **kwargs):
        form = self.form_class(request.POST)
