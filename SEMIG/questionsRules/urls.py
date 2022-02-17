from django.urls import path

from . import views

app_name = "questionsRules"
urlpatterns = [
    # /questionsRules/
    path("", views.IndexView.as_view(), name= "index"),
    # /questionsRules/5
    path("<int:pk>/", views.DetailView.as_view(), name= "detail"),
    # /questionsRules/results
    path("<int:question_id>/results/", views.results, name= "results"),
]
