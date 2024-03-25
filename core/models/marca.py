from django.db import models


class Marca(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.nome} ({self.id})"

    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"
