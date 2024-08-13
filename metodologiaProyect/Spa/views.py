#Las vistas son funciones en Python que procesan las peticiones HTTP y devuelven una respuesta, generalmente 
# un archivo HTML
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .models import Post
from django.urls import reverse_lazy
from django.shortcuts import redirect

def home_redirect(request):
    return redirect('/Spa')

def home(request):
    
    context ={
        
        'posts':Post.objects.all()
    }
    return render(request, 'spa/home.html', context)

class PostListView(ListView):
    model=Post
    template_name= 'Spa/home.html'
    context_object_name= 'posts'
    ordering=['-fecha_posteo']
    paginate_by=5
    
#ver los post del usuario
class UserPostListView(ListView):
    model=Post
    template_name= 'Spa/user_posts.html'
    context_object_name= 'posts'
    ordering=['-fecha_posteo']
    paginate_by=5   
    
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(autor=user).order_by('fecha_posteo')

class PostDetailView(DetailView):
    model=Post
    template_name = 'Spa/post_detail.html'
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model=Post
    fields = ['titulo', 'contenido']
    
    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model=Post
    fields = ['titulo', 'contenido']
    
    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.autor:
            return True
        return False
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('Inicio-Spa')  # Ensure this matches the URL pattern name

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.autor:
            return True
        return False
    
def about(request):
    return render(request, 'spa/About.html', {'title': 'about'})
# Create your views here.
