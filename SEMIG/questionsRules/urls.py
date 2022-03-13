from django.urls import path

from . import views

app_name = "questionsRules"
urlpatterns = [
    # /questionsRules/
    # path("", views.IndexView.as_view(), name= "index"),
    path("", views.index, name= "index"),
    path("prueba/", views.prueba, name= "prueba"),
    path("<int:question_id>/rules/", views.rules, name= "rules"),
    path("<int:question_id>/resp/", views.resp, name= "resp"),
    path("<int:question_id>/gorgojo_info/", views.gorgojoInformation, name= "gorgojoInformation"),
    path("<int:question_id>/gorgojo_info_and_good_practices/", views.gorgojoInformationAndGoodPractice, name= "gorgojoInformationAndGoodPractice"),
    path("<int:question_id>/good_practices/", views.goodPractices, name= "goodPractices"),
    path("<int:question_id>/preventives_measures/", views.preventiveMeasures, name= "preventiveMeasures"),
    # /questionsRules/5
    path("<int:pk>/", views.DetailView.as_view(), name= "detail"),
    # /questionsRules/results
    path("<int:question_id>/results/", views.results, name= "results"),
]
