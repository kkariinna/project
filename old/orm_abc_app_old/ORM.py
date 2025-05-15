'''
https://docs.djangoproject.com/en/4.1/ref/models/querysets/
https://docs.djangoproject.com/en/4.1/ref/models/
https://docs.djangoproject.com/en/4.1/ref/models/fields/
'''


from django.db import models
from orm_abc_app.models import Abc

new_obj = Abc(task='new_task')
new_obj.save()

Abc.objects.all()
for e in Abc.objects.all():
    print(e.name)

Abc.objects.all().order_by('id').reverse()
Abc.objects.values('task', 'current_date').order_by('-id')
Abc.objects.values().filter(id__gte=27).order_by('-id')[0:1][0]['task']
Abc.objects.all().order_by('-id')[:1][0]
Abc.objects.values('id')[2:3]
Abc.objects.values()[2:4][0]['id']

Abc.objects.all()[2:4]
Abc.objects.values_list()
Abc.objects.values_list('task')[:1]
Abc.objects.values_list()[2:4][1][1]
Abc.objects.values_list('id','task').order_by('id').reverse()[:3]

Abc.objects.filter(id__gte=27).delete()
del_obj = Abc.objects.filter(id__gte=27)
del_obj.delete()
Abc.objects.values_list('id').order_by('id').reverse()[:3]


Abc.objects.filter(id__gte=22).update(task = "update")
upd_obj = Abc.objects.filter(id__gte=22)
upd_obj.update(task = "update", b=1)
Abc.objects.values_list('id','task').order_by('id').reverse()[:3]


from django.db import connection
connection.queries
from django.db import reset_queries
reset_queries()

Abc.objects.all().order_by('-pk')
Abc.objects.all().reverse()
Abc.objects.values('pk', 'b').filter(b__gte=6)
Abc.objects.values('pk', 'b').get(pk=11)
Abc.objects.get(pk=11)
object = Abc.objects.get(pk=11)
object.current_date


object = Abc.objects.get(pk=11)
Abc.objects.filter(task__contains='Ра')
Abc.objects.filter(task__icontains='Ра')
Abc.objects.filter(task__contains='Ра').count()
connection.queries
Abc.objects.filter(task__icontains='на', id__gte=17)
Abc.objects.filter(task__icontains='на', id__gte=17).count()
cur_objects = Abc.objects.filter(task__icontains='на', id__gte=15)
cur_objects.values('b')
cur_objects = Abc.objects.filter(id__gte=17) & Abc.objects.filter(c__gte=15)

from django.db.models import Q
Abc.objects.filter(Q(id__gte=17) & Q(c__gte=15))
Abc.objects.filter(Q(id__gte=17) & Q(c__gte=15)).values() - - все поля
Abc.objects.filter(Q(id__gte=17) & Q(c__gte=15)).values().first()

cur_objects.count()
cur_objects.earliest("current_date")
cur_objects.values().earliest("current_date")

Агрегируем
from django.db.models import *
cur_objects = Abc.objects.all()
cur_objects.values('id')
cur_objects.aggregate(Count('id'))
cur_objects.aggregate(Avg('id'))
cur_objects.aggregate(Min('id'))
cur_objects.aggregate(Max('id'))
cur_objects.aggregate(StdDev('id'))
cur_objects.aggregate(Sum('id'))


cur_objects.aggregate(res = Sum('id') - Count('id'))
result = cur_objects.aggregate(res = Sum('id') - Count('id'))
result['res']
result = cur_objects.values('id').aggregate(res = Sum('id') - Count('id'))

for item in cur_objects.values():
    print(item['id'], item['c'])

(Abc.objects.filter(id__gte=17) & Abc.objects.filter(c__gte=15)).values('c').annotate(Count('id'))
r = (Abc.objects.filter(id__gte=17) & Abc.objects.filter(c__gte=15)).values('c')
r.all()
r.annotate(Count('c'))
r.annotate(Sum('c'))

функции
obj = Abc.objects.filter(Q(id__gte=17) & Q(c__gte=15)).values('task').first()
obj = Abc.objects.filter(Q(id__gte=17) & Q(c__gte=15)).values().first()
obj['task'].__len__()


from django.db.models.functions import Abc
from django.db.models.functions import *

q = Abc.objects.values().annotate(a1 = Abs('c')+2)
q.values('a1')
q.values('a1')[3]
from django.db.models.functions import Power
q = Abc.objects.values().annotate(pw = Power('b','c'))
q.values('b', 'c', 'pw')
q.aggregate(Sum('pw'))

res = Abc.objects.values().annotate(r = Random())
res.values_list('r')

res = Abc.objects.values().annotate(r = 'a'*'b')
res.values_list('r')


x = Abc.objects.raw('SELECT * FROM orm_abc_app.Abc')
x.model.objects.values()
