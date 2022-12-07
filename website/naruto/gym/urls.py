from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="gym"),
    path("supp/", views.supp, name="supp"),
    path("contact/", views.ccontact, name="contact"),
    path("trans/", views.trans, name="trans"),
    path("bmr/", views.bmr, name="bmr"),
    path("ninja/", views.create_ninja, name="ninja"),
    path("saiyan/", views.saiyan, name="saiyan"),
    path("tonned/", views.tonned, name="tonned"),
    path("muscle/", views.muscle, name="muscle"),
    path("dis/", views.dis, name="dis"),
    path("healthy/", views.health, name="health"),
  

]