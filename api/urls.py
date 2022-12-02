from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
	path('mitre/<str:mitre_id>', views.MitreAttckView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
