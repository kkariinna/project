import datetime

from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect
# from django.db.models import *
from django.db.models import Count, Avg, Min, Max, StdDev, Sum

from .forms import CreateAbcForm
from .models import Abc


def index(request):
    return render(request, 'index.html')


def var_list_dict(request):
    var_main = 2
    print(var_main)
    list_main = (1, 2, 3, 4, 5)
    print(list_main)
    dict_main = {'x': 1, 'y': 2}
    print(dict_main)
    context = {"var_main": var_main, 'list_main': list_main, 'dict_main': dict_main}
    return render(request, 'list_dict.html', context)


class AbcFormCreate(forms.Form):
    a = forms.IntegerField(initial=1, min_value=2)
    b = forms.IntegerField(required=False)
    c = forms.IntegerField(label='c_lable')


def abc_form(request):
    abc_form = AbcFormCreate()
    print(abc_form)
    return render(request, 'abc_form.html', {"abc_form": abc_form})


def abc_get(request):
    print(request.GET)
    print(request.GET.get("a"))
    print(request.GET.get("b"))
    print(request.GET.get("c"))
    A = request.GET.get("a")
    B = request.GET.get("b")
    C = request.GET.get("c")
    return HttpResponse(f"""
    <pre>
    A = {A}
    B = {B}
    C = {C}
    </pre>
    """)


# def index(request):
#     name_main="index"
#     redirect_url=reverse ('index', args=(name_main))
#     return render(request, redirect_url)


def datetime_nov(request):
    datetime_now = datetime.datetime.now()
    print(datetime_now)
    context = {'key': datetime_now}
    return render(request, 'datetime_now.html', context)


def form_create_0(request):
    print('request.method: ', request.method)
    if request.method == 'POST':
        form = CreateAbcForm(request.POST)
        if form.is_valid():
            print("\nform_is_valid:\n", form)
            form.save()
            return redirect('orm_abc_app:form_result')
    else:
        form = CreateAbcForm()
        print('\nform_else:\n', form)
    context = {'form': form}
    print("\ncontext:\n", context)
    return render(request, 'form_create_0.html', context)


def form_create(request):
    print('request.method: ', request.method)
    if request.method == 'POST':
        form = CreateAbcForm(request.POST)
        if form.is_valid():
            print("\nform_is_valid:\n", form)
            form.save()
            return redirect('orm_abc_app:form_result')
    else:
        form = CreateAbcForm()
        print('\nform_else:\n', form)
    context = {'form': form}
    print("\ncontext:\n", context)
    return render(request, 'form_create.html', context)


def form_result(request):
    object = Abc.objects.all().order_by('-id')[:1]
    print("object: ", object)
    # dict
    row = object.values('a', 'b', 'c')[0]
    print("row: ", row)
    print("row_a: ", row['a'])
    # list
    row_list = object.values_list()[0]
    print("row_list: ", row_list)
    if row_list[2] + row_list[3] == row_list[4]:
        result = " С равна сумме A и B"
    else:
        result = "С не равна сумме A и B"
    # context
    task = row_list[1]
    print('task: ', task)
    last_data = [row_list[2], row_list[3], row_list[4]]
    print('last_data:', last_data)
    print('result: ', result)

    context = {'task': task, 'last_data': last_data, 'result': result, 'row': row}
    return render(request, 'form_result.html', context)


def table(request):
    row = Abc.objects.values()
    print('row:', row)
    row_lists = Abc.objects.values_list()
    print('row_lists:', row_lists)
    cur_objects = Abc.objects.all()
    statics_val = [cur_objects.aggregate(Count('b')), cur_objects.aggregate(Avg('b')), cur_objects.aggregate(Min('b')),
                   cur_objects.aggregate(Max('b')), cur_objects.aggregate(StdDev('b')), cur_objects.aggregate(Sum('b'))]
    print(statics_val)
    statics = {'statics_val': statics_val}

    fields = Abc._meta.get_fields()
    print(fields)
    verbose_name_list = []
    name_list = []
    for e in fields:
        verbose_name_list.append(e.verbose_name)
        name_list.append(e.name)
    print(verbose_name_list)
    print(name_list)
    field_names = verbose_name_list
    context = {'row': row, 'row_lists': row_lists, 'field_names': field_names, 'statics': statics}
    return render(request, 'table.html', context)
