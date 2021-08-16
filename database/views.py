from django.conf import settings
from django.contrib import messages
from django.utils import timezone

from django.shortcuts import render, redirect

from database.models import Seminar, Person, Registration


def signup_form(request):
    context = {
        'seminars': sorted(Seminar.objects.filter(date_and_time__gt=timezone.now()), key=lambda x: x.date_and_time),
        'merchant_id': settings.PAYFAST_MERCHANT_ID,
        'merchant_key': settings.PAYFAST_MERCHANT_KEY
    }
    return render(request, 'database/signup_form.html', context=context)


def initial_payment_info_is_valid(post_data):
    return True


def register(request):
    # TODO: First check if the data is valid, either with some code or JS on the page...
    if request.method == "POST":
        return_from_payment = False

        if return_from_payment:
            # TODO: Think about if I should check if the person already exists
            # Make the parent
            parent = Person(first_name=request.POST['parentFirstName'],
                            last_name=request.POST['parentLastName'],
                            email_address=request.POST['parentEmail'],
                            cellphone_number=request.POST['parentPhoneNumber'])
            # Make the student
            student = Person(first_name=request.POST['studentFirstName'],
                             last_name=request.POST['studentLastName'],
                             email_address=request.POST['studentEmail'],
                             cellphone_number=request.POST['studentPhoneNumber'])

            parent.save()
            student.save()

            parent_accepts_waiver = 'parentCovidWaiver' in request.POST
            student_accepts_waiver = 'studentCovidWaiver' in request.POST

            time_registered = timezone.now()

            registration = Registration(parent_guardian=parent,
                                        parent_guardian_accepts_waiver=parent_accepts_waiver,
                                        child=student,
                                        child_accepts_waiver=student_accepts_waiver,
                                        additional_info=request.POST['additionalInfoTextArea'],
                                        time_registered=time_registered)

            registration.save()

            for ticked_seminar in request.POST:
                if ticked_seminar.startswith('seminarCheckBox'):
                    seminar_id = ticked_seminar.replace('seminarCheckBox', '')
                    seminar = Seminar.objects.filter(id=seminar_id).first()
                    registration.registered_seminars.add(seminar)

        else:
            if initial_payment_info_is_valid(request.POST):
                return redirect(settings.PAYFAST_URL)
            else:
                messages.error("There was an error with your details. Please try again.")

    return redirect("signup-form")
