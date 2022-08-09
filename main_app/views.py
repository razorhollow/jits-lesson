from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from .models import Technique

# Create your views here.
class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def technique_index(request):
  techniques = Technique.objects.filter(user=request.user)
  return render(request, 'techniques/index.html', { 'techniques': techniques })

@login_required
def technique_detail(request, technique_id):
  technique = Technique.objects.get(id=technique_id)
  return render(request, 'techniques/detail.html', { 'technique': technique })

class TechniqueCreate(LoginRequiredMixin, CreateView):
  model = Technique
  fields = ['name', 'description', 'category', 'video']
  success_url = '/techniques/'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class TechniqueUpdate(LoginRequiredMixin, UpdateView):
  model = Technique
  fields = ['name', 'description', 'category', 'video']

class TechniqueDelete(LoginRequiredMixin, DeleteView):
  model = Technique
  success_url = '/techniques/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('technique_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)