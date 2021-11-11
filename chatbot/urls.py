from django.urls import re_path
from .views import trainModel,testModel,activateModel

urlpatterns = [
    re_path(r"^train/?$",trainModel.as_view()), #te ayuda a entrenar el modelo
    re_path(r"^test/?$",testModel.as_view()),   #interfaz que te va a yudar a probar el chatbot, para saber si reponde bien
    re_path(r"^activate/?$",activateModel.as_view())  # qué elemento de la bd esta activo en es e momento
]