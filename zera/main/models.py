from django.db import models
from django.core.validators import MaxValueValidator


class Feedback(models.Model):
    name = models.CharField('Имя', max_length=50)
    quality = models.IntegerField('Оценка', validators=[MaxValueValidator(5)])
    feedback = models.TextField('Отзыв')

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField('Услуга', max_length=50, db_index=True)

    def __str__(self):
        return self.name


class ServiceCategory(models.Model):
    name = models.CharField('Вид услуги', max_length=50, null=True)
    min_price =  models.IntegerField('Минимальная цена', null=False)
    max_price =  models.IntegerField('Максимальная цена', null=True, blank=True)

    service = models.ForeignKey('Service', on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class Portfolio(models.Model):
    image = models.ImageField(upload_to='main/files/port_images')