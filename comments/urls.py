from django.urls import path

from .views import CrearComentarioView, ResponderComentarioView, ListarComentariosView

urlpatterns = [
    path("comments/", CrearComentarioView.as_view(), name="createComment"), #Post de un comentario
    path("comments/list", ListarComentariosView.as_view(), name="listComments"), #Obtener los comentarios
    path("comments/<int:responseCommentId>/reply", ResponderComentarioView.as_view(), name="replyComment"), #Post de una respuesta a un comentario a una respuesta
]