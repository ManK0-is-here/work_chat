from django.contrib import admin
from django.db.models import Count
from .models import *


class ProblemList(admin.SimpleListFilter):
    title = "Статус задач"