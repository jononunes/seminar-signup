from django.shortcuts import render

from database.models import Seminar


def signup_form(request):
    context = {'seminars': Seminar.objects.all()}
    return render(request, 'database/signup_form.html', context=context)
