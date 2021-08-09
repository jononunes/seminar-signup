from django.shortcuts import render


def signup_form(request):
    return render(request, 'database/signup_form.html')
