from django.urls import path,include
# from .views import user_profile
from . import views
from rest_framework import routers
from .views import job_seekerViewSet,companyViewSet,post_jobsViewSet,apply_jobViewSet

router = routers.DefaultRouter()
router.register ('jobseekers',job_seekerViewSet),
router.register ('companies',companyViewSet),
router.register ('post_jobs',post_jobsViewSet),
router.register ('apply_job',apply_jobViewSet),

urlpatterns = [
    path('login/',views.login, name ='login'),
    # path('profile/', user_profile, name='user_profile'),
    path('delete/<int:pk>',views.comp_delete, name ='delete'),
    path('register/job-seeker/', views.register_job_seeker, name='register_job_seeker'),
    path('register/company/', views.register_company, name='register_company'),
    path('dashboard/job-seeker/', views.job_seeker_dashboard, name='job_seeker_dashboard'),
    path('dashboard/company/', views.company_dashboard, name='company_dashboard'),
    path('post-job/', views.post_job, name='post_job'),
    path('apply-job/<int:job_id>/', views.apply_for_job, name='apply_for_job'),
    path('api/',include(router.urls))
]
