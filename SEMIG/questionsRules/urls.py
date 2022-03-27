from django.urls import path

from . import views

app_name = "questionsRules"
urlpatterns = [
    # /questionsRules/
    # path("", views.IndexView.as_view(), name= "index"),
    path("", views.index, name= "index"),
    path("pag_not_found/", views.pagError, name="pagError"),
    path("prueba/", views.prueba, name= "prueba"),
    path("<int:question_id>/rules/", views.rules, name= "rules"),
    path("<int:question_id>/resp/", views.resp, name= "resp"),
    path("<int:question_id>/gorgojo_info/", views.gorgojoInformation, name= "gorgojoInformation"),
    path("<int:question_id>/gorgojo_info_and_good_practices/", views.gorgojoInformationAndGoodPractice, name= "gorgojoInformationAndGoodPractice"),
    path("<int:question_id>/good_practices/", views.goodPractices, name= "goodPractices"),
    path("<int:question_id>/preventives_measures/", views.preventiveMeasures, name= "preventiveMeasures"),
    path("<int:question_id>/chemicals/", views.chemicals, name= "chemicals"),
    path("<int:question_id>/ditches/", views.ditches, name= "ditches"),
    path("<int:question_id>/plant_other_vegetables/", views.plantOtherVegetables, name= "plantOtherVegetables"),
    path("<int:question_id>/plant_pick_up/", views.plantPickUp, name= "plantPickUp"),
    path("<int:question_id>/traps/", views.traps, name= "traps"),
    path("<int:question_id>/continue_stage_choice/", views.continueStageChoice, name= "continueStageChoice"),
    path("<int:question_id>/cultural_work/", views.culturalWork, name= "culturalWork"),
    path("<int:question_id>/gorgojo_measures/", views.gorgojoMeasures, name= "gorgojoMeasures"),
    path("<int:question_id>/gather_gorgojo/", views.gatherGorgojo, name= "gatherGorgojo"),
    path("<int:question_id>/counther_the_gorgojo/", views.countherTheGorgojo, name= "countherTheGorgojo"),
    path("<int:question_id>/potato_selection/", views.potatoSelection, name= "potatoSelection"),
    path("<int:question_id>/soil_removal/", views.soilRemoval, name= "soilRemoval"),
    path("<int:question_id>/warehouse_preparation/", views.warehousePreparation, name= "warehousePreparation"),
    path("<int:question_id>/danger_into_warehouse/", views.dangerIntoWarehouse, name= "dangerIntoWarehouse"), 
    path("<int:question_id>/white_fungus/", views.whiteFungus, name= "whiteFungus"), 
]
