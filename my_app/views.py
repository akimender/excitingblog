from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from .models import Blog, Comment
from .forms import BlogForm, CommentForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse

# Create your views here.
class Home(LoginView):
  template_name = 'home.html'

@login_required
def index(request):
  if request.method == 'POST':
    form = BlogForm(request.POST)
    if form.is_valid():
      blog = form.save(commit=False)
      blog.user = request.user
      blog.save()
      return redirect('index')
  else:
    form = BlogForm()
    blogs = Blog.objects.all()
    return render(request, 'index.html', {'form': form, 'blogs': blogs})

@login_required
def blog_detail(request, pk):
  blog = Blog.objects.get(id=pk)
  if request.method == 'POST':
    form = CommentForm(request.POST)
    if form.is_valid():
      comment = form.save(commit=False)
      comment.user = request.user
      comment.blog = blog
      comment.save()
      return redirect('blog-detail', pk=blog.id)
  else:
    form = CommentForm()
    comments = blog.comments.all()
    return render(request, 'blogs/detail.html', {'form': form, 'blog': blog, 'comments': comments})

class BlogUpdate(UpdateView):
  model = Blog
  fields = ['title', 'description']
  template_name = 'blogs/edit.html'

  def get_success_url(self):
    return reverse('blog-detail', kwargs={'pk': self.object.pk})
  
class BlogDelete(DeleteView):
  model = Blog
  success_url = '/blogs/'

class CommentUpdate(DeleteView):
    model = Comment
    success_url = '/blogs/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign-up - try again'
  
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)
  