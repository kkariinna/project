# import datetime
from django.db import models

c_choices = (
    (0, "ноль"),
    (10, "десять"),
    (15, "пятнадцать"),
    (20, "двадцать"),
)


class Abc(models.Model):
    task = models.CharField("Формулировка задачи", default="Равна ли С сумме A и B ?", max_length=256)
    a = models.IntegerField("Значение А", default=0, )
    b = models.IntegerField("Значение B", default=0, help_text="Подсказка для поля")
    c = models.IntegerField("Значение С", choices=c_choices, default=0, )
    current_date = models.DateTimeField("Дата записи", auto_now=True)

    def __str__(self):
        # return self.task
        # return '%s %s' % (self.task, self.current_date)
        return f"{self.id}&{self.task}"


    class Meta:
        verbose_name = "A_B_C"
        verbose_name_plural = "A_B_C_S"
        ordering = ('-id', '-a')




# current_date = models.DateTimeField("ДатаВремя", default=datetime.datetime.now())
# current_date = models.DateTimeField("ДатаВремя", auto_now_add=True)


# python manage.py makemigrations
# python manage.py migrate


# admin.py
# from django.contrib import admin
# # Register your models here.
# from .models import Abc
# admin.site.register(Abc)


# forms.py
# from django.forms import ModelForm
# from .models import Abc
#
# class CreateAbcForm(ModelForm):
#     class Meta:
#         model = Abc
#         fields = ['task', 'a' ,'b' ,'c', 'c_calc']
