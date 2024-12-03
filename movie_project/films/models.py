from django.db import models

class Film(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название фильма')
    description = models.TextField(verbose_name='Описание фильма')
    review = models.TextField(verbose_name='Отзыв о фильме')
    image = models.ImageField(upload_to='films/', blank=True, null=True, verbose_name='Изображение')

    def __str__(self):
        return self.title