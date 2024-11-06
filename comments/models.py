from django.db import models

class Comentario(models.Model):
    content = models.TextField() #Contenido del comentario
    responseComment = models.ForeignKey('self',on_delete=models.CASCADE, related_name='replies', null=True, blank=True) #Comentario padre (Puede ser null y se relaciona de uno a muchos)

    def __str__(self) -> str:
        return self.content
