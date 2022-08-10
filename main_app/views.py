from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from .models import Technique, Category_Index

CATEGORY_Q = (
  ('CG', 'Closed Guard'),
  ('BG', 'Butterfly  Guard'),
  ('SG', 'Spider Guard'),
  ('LG', 'Lasso Guard'),
  ('DLR', 'De La Riva Guard'),
  ('HGB', 'Half Guard Bottom'),
  ('HGT', 'Half Guard Top'),
  ('SCB', 'Side Control Bottom'),
  ('SCT', 'Side Control Top'),
  ('MT', 'Mount Top'),
  ('ME', 'Mount Escape'),
  ('BC', 'Back Control'),
  ('BE', 'Back Escape'),
  ('KOB', 'Knee On Belly'),
  ('NS', 'North South'),
  ('GP', 'Guard Pass'),
  ('GR', 'Guard Retention'),
  ('TD', 'Takedown'),
  ('OT', 'Other')
)

# Create your views here.
class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

def lesson_plan(request):
  index = Category_Index.objects.first().index
  weekly_category = CATEGORY_Q[index][0]
  techniques = Technique.objects.filter(category=weekly_category)[:6]
  return render(request, 'techniques/plan.html', {'index': index, 'weekly_category': weekly_category, 'techniques': techniques})

@login_required
def load_plan(request):
  index = Category_Index.objects.first().index
  weekly_category = CATEGORY_Q[index][0]
  techniques = Technique.objects.filter(category=weekly_category)[:6]
  for technique in techniques:
    technique.counter += 1
    technique.save()
  index_object = Category_Index.objects.first()
  if index_object.index >= (len(CATEGORY_Q))-1:
    index_object.index = 0
  else:
    index_object.index += 1
  index_object.save()
  return redirect('lesson_plan')

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