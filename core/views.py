from django.shortcuts import render

def start_page(request):
    context = {
        "title": "То что поможет в работе"
    }
    return render(request, "start_page.html", context)
