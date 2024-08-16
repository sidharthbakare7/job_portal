from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import job_seeker, company, post_jobs, apply_job
from .forms import JobSeekerForm, CompanyForm, PostJobForm, ApplyJobForm
from rest_framework import viewsets
from .serializers import job_seekerSerializer,companySerializer,post_jobsSerializer,apply_jobSerializer

@login_required
def user_profile(request):
    user = request.user
    try:
      profile = job_seeker.objects.get(user=user)
      profile_type = 'Job Seeker'
    except job_seeker.DoesNotExist:
       profile = company.objects.get(user=user)
       profile_type = 'Company'
    # Pass the profile and type to the template
    context = {
        'profile': profile,
        'profile_type': profile_type,
    }
    return render(request, 'user_profile.html', context)


def register_job_seeker(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        profile_form = JobSeekerForm(request.POST, request.FILES)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit = False)
            profile.user = user
            profile.save()
            login(request,user)
            return redirect('job_seeker_dashboard')
    else:
        form = UserCreationForm()
        profile_form = JobSeekerForm()
    return render(request, 'register_job_seeker.html', {'form': form, 'profile_form': profile_form})

def register_company(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        profile_form = CompanyForm(request.POST, request.FILES)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit = False)
            profile.user = user
            profile.save()
            login(request)
            return redirect('company_dashboard')
    else:
        form = UserCreationForm()
        profile_form = CompanyForm()
    return render(request, 'register_company.html', {'form': form, 'profile_form': profile_form})

def login (request):
    if request.method=="POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user =form.get_user()
            auth_login(request,user)
            return redirect('job_seeker_dashboard.html')
    else:
        form = AuthenticationForm()
    return render(request,'login.html', {'form': form})

# Job Seeker Dashboard
@login_required
def job_seeker_dashboard(request):
    jobs = post_jobs.objects.all()
    return render(request, 'job_seeker_dashboard.html', {'jobs': jobs})

# Company Dashboard
@login_required
def company_dashboard(request):
    jobs = post_jobs.objects.filter(company__user=request.user)
    return render(request, 'company_dashboard.html', {'jobs': jobs})
# Post a Job
@login_required
def post_job(request):
    if request.method == 'POST':
        form = PostJobForm(request.POST, request.FILES)
        if form.is_valid():
            job = form.save(commit=False)
            job.company = company.objects.get(user=request.user)
            job.save()
            return redirect('company_dashboard')
    else:
        form = PostJobForm()
    return render(request, 'post_job.html', {'form': form})

# Apply for a Job
@login_required
def apply_for_job(request,job_id):
    job = post_jobs.objects.get(id=job_id)
    if request.method == 'POST':
        form = ApplyJobForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.applicant = job_seeker.objects.get(user=request.user)
            application.job = job
            application.save()
            return redirect('job_seeker_dashboard')
    else:
        form = ApplyJobForm()
    return render(request, 'apply_for_job.html', {'form': form, 'job': job})

def comp_delete(request,pk):
    comp= get_object_or_404(company,pk=pk)
    comp.delete()
    return redirect('company_dashboard') 

class job_seekerViewSet( viewsets.ModelViewSet):
     queryset = job_seeker.objects.all()
     serializer_class= job_seekerSerializer

class companyViewSet(viewsets.ModelViewSet):
     queryset = company.objects.all()
     serializer_class= companySerializer


class post_jobsViewSet(viewsets.ModelViewSet):
     queryset = post_jobs.objects.all()
     serializer_class= post_jobsSerializer


class apply_jobViewSet(viewsets.ModelViewSet):
     queryset = apply_job.objects.all()
     serializer_class= apply_jobSerializer
