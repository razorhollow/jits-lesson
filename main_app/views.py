from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Technique

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def technique_index(request):
  techniques = Technique.objects.all()
  return render(request, 'techniques/index.html', { 'techniques': techniques })

def technique_detail(request, technique_id):
  technique = Technique.objects.get(id=technique_id)
  return render(request, 'techniques/detail.html', { 'technique': technique })

class TechniqueCreate(CreateView):
  model = Technique
  fields = ['name', 'description', 'category', 'video']
  success_url = '/techniques/'

class TechniqueUpdate(UpdateView):
  model = Technique
  fields = ['name', 'description', 'category', 'video']

class TechniqueDelete(DeleteView):
  model = Technique
  success_url = '/techniques/'