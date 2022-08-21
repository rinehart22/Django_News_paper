from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm 




class SignUpView(CreateView):
	form_class=CustomUserCreationForm
	url = reverse_lazy('login')
	template_name = 'signup.html'


