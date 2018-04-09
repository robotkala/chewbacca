from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from clients import views

urlpatterns = [
    url(r'^clients/$', views.ClientList.as_view()),
    url(r'^clients/(?P<pk>[0-9]+)/$', views.ClientDetail.as_view()),
    url(r'^workout_plans/$', views.WorkoutPlanList.as_view()),
    url(r'^workout_plans/(?P<pk>[0-9]+)/$', views.WorkoutDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
