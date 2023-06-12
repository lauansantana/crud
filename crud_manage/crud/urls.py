from django.urls import path
from .views import *

urlpatterns = [
    path("",home),
    path("home/",home),
    path("add-estudante/", crud_add),
    path("delete-crud/<int:matricula>", delete_crud),
    path("atualizar-crud/<int:matricula>", atualizar_crud),
    path("a-atualizar-crud/<int:matricula>", a_atualizar_crud)

]
