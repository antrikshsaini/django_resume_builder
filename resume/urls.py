from django.urls import path
from .views import ResumeView

urlpatterns = [
    path('', ResumeView.as_view(), name='resume-create'),
    path('<int:id>/', ResumeView.as_view(), name='resume-detail'),
    path('all/', ResumeView.as_view(), name='resume-list'),
]
