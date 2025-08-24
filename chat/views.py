from django.shortcuts import render

# Create your views here.
def group_create(r):
    return render(r, "group_create.html")
