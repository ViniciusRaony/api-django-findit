from django.db import models


# Create your models here.
class Cadastro(models.Model):
    titulo = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo

    class Meta:
        db_table = "cadastro"
