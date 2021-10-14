from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,ListView,UpdateView
from .models import MyUser,Order,Product
from .forms import SignInForm,SignUpForm
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse_lazy
# Create your views here.

class SignUpView(CreateView):
    model=MyUser
    form_class = SignUpForm
    template_name = 'user/signup.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['form']=self.form_class
        return context

class SignInViews(TemplateView):
    form_class= SignInForm
    template_name = 'user/signin.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['form']=self.form_class
        return context

    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
            else:
                return redirect('home')
        else:
            return redirect('signup')


class Home(TemplateView):
    template_name = 'user/home.html'
