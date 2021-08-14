from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email_address = models.EmailField()
    cellphone_number = models.CharField(max_length=11, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def __eq__(self, other):
        return self.first_name == other.first_name and \
               self.last_name == other.last_name and \
               self.email_address == other.email_address and \
               self.cellphone_number == other.cellphone_number


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
    base_price = models.DecimalField(max_digits=8, decimal_places=2)
    course_content = models.TextField()
    capacity = models.IntegerField(default=20)

    def __str__(self):
        return f"{self.subject} - {self.level} [{self.date_and_time}]"


class Registration(models.Model):
    parent_guardian = models.OneToOneField(Person, models.CASCADE, related_name="parent_guardian")
    parent_guardian_accepts_waiver = models.BooleanField()
    child = models.OneToOneField(Person, models.CASCADE, related_name="child")
    child_accepts_waiver = models.BooleanField()
    registered_seminars = models.ManyToManyField(Seminar)
    additional_info = models.TextField(blank=True, default="")
    time_registered = models.DateTimeField(default=None)

    def __str__(self):
        return f"{self.child}"


class Payment(models.Model):
    amount_paid = models.DecimalField(max_digits=8, decimal_places=2)
    registration = models.ForeignKey(Registration, on_delete=models.CASCADE)

    def __str__(self):
        return f"R{self.amount_paid} - {self.registration.parent_guardian} / {self.registration.child}"
