from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
	path('pyattck/', views.MyAttckView.as_view()),
	path('mitre/', views.MitreAttck.as_view()),
	path('mitrepost/', views.MitreAttck.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
