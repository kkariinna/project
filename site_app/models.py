from django.db import models
from django.urls import reverse

class Item(models.Model):

    item_title = models.CharField(verbose_name = 'Заголовок (title)', max_length=255, default="Заголовок" )

    item_nav = models.CharField(verbose_name = 'Название ссылки', max_length=255, default="Название ссылки")

    item_nav_position = models.IntegerField(verbose_name = 'Приоритет ссылки в навигации (0 - исключить)', default=1, help_text="большее - число правее, 0 - исключить из навигации")

    item_content = models.TextField(verbose_name = 'Основное содержание страницы', 
    default = '<a id="top_of _page" href="#h1" class="card-link">На раздел 1</a>   <h6 class="card-subtitle mb-2 text-body-secondary ">   <a id="h1">Раздел 1</a></h6>   <p class="card-text">Содержание раздела 1</p>   <img src="/static/images/settings_django.png"  height="30px">    <a href="#top_of _page" class="card-link">к началу страницы</a>')
    
    item_current_date = models.DateTimeField(verbose_name = "Дата Записи", auto_now=True)

    class Meta:
        verbose_name = 'Содержание текущей страницы'
        verbose_name_plural = 'Содержание всех страниц'
        ordering = ('-item_nav_position',)

    def __str__(self):
        return f"pk: {self.pk};  item_title: {self.item_title}"

