from django.shortcuts import render
from django.views.generic import (ListView, CreateView, 
                                 DeleteView, UpdateView, 
                                 DetailView)
from ProyectoFinal.models import Post
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from ProyectoFinal.forms import UsuarioForm
from ProyectoFinal.models import Avatar, Post, Mensaje
from django.contrib.auth.models import User

@login_required
def index(request):
    posts = Post.objects.order_by ('-publicado_el').all()
    return render(request, "ProyectoFinal/index.html", {"posts": posts})

class PostDetalle (DetailView):
    model = Post

class PostListar(ListView):
    model = Post
    
class PostCrear(LoginRequiredMixin, CreateView):
    model = Post
    success_url = reverse_lazy ("ProyectoFinal-Listar")
    fields = '__all__'
    
class PostBorrar (LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy ("ProyectoFinal-Listar")
    
class PostActualizar (LoginRequiredMixin, UpdateView):
    model = Post
    success_url = reverse_lazy ("ProyectoFinal-Listar")
    fields = "__all__"    

class UserSignUp (CreateView):
    form_class = UsuarioForm 
    template_name = 'registration/signup.html'
    success_url = reverse_lazy ('ProyectoFinal-Listar')
    
class UserLogin (LoginView):
    next_page = reverse_lazy ('ProyectoFinal-Listar')
    
class UserLogout (LogoutView):
    next_page = reverse_lazy ('ProyectoFinal-Index')
    
class AvatarActualizar (UpdateView):
    model = Avatar
    fields = ['imagen']
    success_url = reverse_lazy ('ProyectoFinal-Listar')
    
class UserActualizar (UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email']
    success_url = reverse_lazy ('ProyectoFinal-Listar')
    
class MensajeDetalle (LoginRequiredMixin, DetailView):
    model = Mensaje
    
class MensajeListar (LoginRequiredMixin, ListView):
    model = Mensaje 
    
class MensajeCrear (LoginRequiredMixin, CreateView):
    model = Mensaje 
    success_url = reverse_lazy ('ProyectoFinal-Mensajes-Crear')
    fields = ['nombre', 'email', 'texto'] 
    success_message = "Mensaje enviado !!"    

class MensajeBorrar (LoginRequiredMixin, DeleteView):
    model = Mensaje
    success_url = reverse_lazy ('ProyectoFinal-Mensajes-Listar')