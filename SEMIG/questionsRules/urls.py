from django.urls import path

from . import views

app_name = "questionsRules"
urlpatterns = [
    # /questionsRules/
    # path("", views.IndexView.as_view(), name= "index"),
    path("", views.index, name= "index"),
    path("objective/", views.objective, name= "objective"),
    path("contact/", views.contact, name= "contact"),
    path("pag_not_found/", views.pagError, name="pagError"),
    path("<int:question_id>/rules/", views.rules, name= "rules"),
    path("<int:question_id>/resp/", views.resp, name= "resp"),
    path("<int:question_id>/gorgojo_info/<tarea>/<sugesstion>", views.gorgojoInformation, name= "gorgojoInformation"),
    path("<int:question_id>/gorgojo_info_and_good_practices/<tarea>/<sugesstion>", views.gorgojoInformationAndGoodPractice, name= "gorgojoInformationAndGoodPractice"),
    path("<int:question_id>/good_practices/<tarea>/<sugesstion>", views.goodPractices, name= "goodPractices"),
    path("<int:question_id>/preventives_measures/<tarea>/<sugesstion>", views.preventiveMeasures, name= "preventiveMeasures"),
    path("<int:question_id>/chemicals/<tarea>/<sugesstion>", views.chemicals, name= "chemicals"),
    path("<int:question_id>/ditches/<tarea>/<sugesstion>", views.ditches, name= "ditches"),
    path("<int:question_id>/plant_other_vegetables/<tarea>/<sugesstion>", views.plantOtherVegetables, name= "plantOtherVegetables"),
    path("<int:question_id>/plant_pick_up/<tarea>/<sugesstion>", views.plantPickUp, name= "plantPickUp"),
    path("<int:question_id>/traps/<tarea>/<sugesstion>", views.traps, name= "traps"),
    path("<int:question_id>/continue_stage_choice/", views.continueStageChoice, name= "continueStageChoice"),
    path("<int:question_id>/cultural_work/<tarea>/<sugesstion>", views.culturalWork, name= "culturalWork"),
    path("<int:question_id>/gorgojo_measures/<tarea>/<sugesstion>", views.gorgojoMeasures, name= "gorgojoMeasures"),
    path("<int:question_id>/gather_gorgojo/<tarea>/<sugesstion>", views.gatherGorgojo, name= "gatherGorgojo"),
    path("<int:question_id>/counther_the_gorgojo/<tarea>/<sugesstion>", views.countherTheGorgojo, name= "countherTheGorgojo"),
    path("<int:question_id>/potato_selection/<tarea>/<sugesstion>", views.potatoSelection, name= "potatoSelection"),
    path("<int:question_id>/soil_removal/<tarea>/<sugesstion>", views.soilRemoval, name= "soilRemoval"),
    path("<int:question_id>/warehouse_preparation/<tarea>/<sugesstion>", views.warehousePreparation, name= "warehousePreparation"),
    path("<int:question_id>/danger_into_warehouse/<tarea>/<sugesstion>", views.dangerIntoWarehouse, name= "dangerIntoWarehouse"), 
    path("<int:question_id>/white_fungus/<tarea>/<sugesstion>", views.whiteFungus, name= "whiteFungus"), 
]
