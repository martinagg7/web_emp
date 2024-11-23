from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Page(models.Model):
    title = models.CharField(verbose_name="Título", max_length=200)
    content = RichTextUploadingField(verbose_name="Contenido")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Edición")
    order = models.SmallIntegerField(verbose_name="Orden", default=0)

    class Meta:
        verbose_name = "página"
        verbose_name_plural = "páginas"
        ordering = ['order','title']

    def __str__(self):
        return self.title