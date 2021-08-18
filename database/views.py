from django.conf import settings
from django.contrib import messages
from django.utils import timezone

from django.shortcuts import render, HttpResponse

from database.models import Seminar, Person, Registration

from django.views.decorators.csrf import csrf_exempt


def signup_form(request):
    context = {
        'seminars': Seminar.get_open_seminars(),
        'closed_seminars': Seminar.get_closed_seminars(),
        'merchant_id': settings.PAYFAST_MERCHANT_ID,
        'merchant_key': settings.PAYFAST_MERCHANT_KEY,
        'payfast_url': settings.PAYFAST_URL,
        'return_url': settings.PAYFAST_RETURN_URL,
        'cancel_url': settings.PAYFAST_CANCEL_URL,
        'notify_url': settings.PAYFAST_NOTIFY_URL,
    }

    return render(request, 'database/signup_form.html', context=context)


@csrf_exempt
def register(request):
    if request.method == "POST":
        # Make the parent
        parent = Person(first_name=request.POST['name_first'],
                        last_name=request.POST['name_last'],
                        email_address=request.POST['email_address'],
                        cellphone_number=request.POST['custom_str5'])

        # Make the student
        # The student info is part of the custom_str1 data
        student_info = request.POST["custom_str1"].split(",")
        student = Person(first_name=student_info[0],
                         last_name=student_info[1],
                         email_address=student_info[2],
                         cellphone_number=student_info[3])

        parent.save()
        student.save()

        covid_info = request.POST["custom_str2"].split(",")
        parent_accepts_waiver = covid_info[0] == "true"
        student_accepts_waiver = covid_info[1] == "true"

        time_registered = timezone.now()

        registration = Registration(parent_guardian=parent,
                                    parent_guardian_accepts_waiver=parent_accepts_waiver,
                                    child=student,
                                    child_accepts_waiver=student_accepts_waiver,
                                    additional_info=request.POST['custom_str4'],
                                    time_registered=time_registered)

        registration.save()

        ticked_seminar_ids = request.POST['custom_str3'].split(",")
        for ticked_seminar_id in ticked_seminar_ids:
            seminar = Seminar.objects.filter(id=ticked_seminar_id).first()
            registration.registered_seminars.add(seminar)

    return HttpResponse(status=200)


def success(request):
    messages.success(request, "You have successfully registered! A confirmation email will be sent to you shortly.")
    return render(request, 'database/signup_form.html')


def cancel(request):
    messages.info(request, "Something has gone wrong with the payment, please try again.")
    return render(request, 'database/signup_form.html')
