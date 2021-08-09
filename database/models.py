from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email_address = models.EmailField()
    cellphone_number = models.CharField(max_length=11, null=True)


class Payment(models.Model):
    amount_paid = models.DecimalField()


class Registration(models.Model):
    parent_guardian = models.ForeignKey(Person, models.CASCADE)
    parent_guardian_accepts_waiver = models.BooleanField()
    child = models.ForeignKey(Person, models.CASCADE)
    child_accepts_waiver = models.BooleanField()


class Seminar(models.Model):
    subject_choices = [
        ("MATHS_P1", "Maths Paper 1"),
        ("MATHS_P2", "Maths Paper 2"),
        ("PHYSICS", "Physics"),
        ("CHEMISTRY", "Chemistry")
    ]
    subject = models.CharField(max_length=15, choices=subject_choices)

    level_choices = [
        ("STANDARD", "Standard"),
        ("ADVANCED", "Advanced")
    ]
    level = models.CharField(max_length=15, choices=level_choices)

    date_and_time = models.DateTimeField()
    base_price = models.DecimalField()

