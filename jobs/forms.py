from django import forms
from .models import job_seeker, company, post_jobs, apply_job

class JobSeekerForm(forms.ModelForm):
    class Meta:
        model = job_seeker
        fields = ['status', 'email', 'phone_number', 'profile_image', 'gender', 'address', 'occupation', 'age', 'user_type', 'bio', 'resume', 'skills', 'experience', 'years_experience', 'company_name', 'company_address', 'position', 'start_date', 'end_date']
        # fields = '__all__'

class CompanyForm(forms.ModelForm):
    class Meta:
        model = company
        fields = ['phone_number', 'email', 'company_logo', 'gender', 'user_type', 'company_name', 'company_ceo', 'company_established', 'company_location', 'status']
        # fields = '__all__'

class PostJobForm(forms.ModelForm):
    class Meta:
        model = post_jobs
        fields = ['title', 'jobtype', 'salary', 'image', 'description', 'experience', 'location', 'status', 'skills']
        # fields = '__all__'
class ApplyJobForm(forms.ModelForm):
    class Meta:
        model = apply_job
        fields = ['company', 'email', 'jobtype', 'resume', 'apply_date', 'status']
        # fields = '__all__'