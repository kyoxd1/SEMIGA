from django.urls import path

from . import views

app_name = "questionsRules"
urlpatterns = [
    # /questionsRules/
    # path("", views.IndexView.as_view(), name= "index"),
    path("", views.index, name= "index"),
    path("<int:question_id>/rules/", views.rules, name= "rules"),
    path("<int:question_id>/resp/", views.resp, name= "resp"),
    path("<int:question_id>/gorgojo_info/", views.gorgojoInformation, name= "gorgojoInformation"),
    # /questionsRules/5
    path("<int:pk>/", views.DetailView.as_view(), name= "detail"),
    # /questionsRules/results
    path("<int:question_id>/results/", views.results, name= "results"),
]
