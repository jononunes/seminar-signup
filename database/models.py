from django.db import models
from django.utils import timezone


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

    def get_all_registrations(self):
        return self.registration_set.all()

    def get_spaces_remaining(self):
        number_of_registrations = len(self.get_all_registrations())
        spaces_remaining = self.capacity - number_of_registrations
        return spaces_remaining

    def is_full(self):
        return self.get_spaces_remaining() <= 0

    @staticmethod
    def get_distinct_subjects():
        all_seminars = Seminar.objects.all()
        ids_to_return = []

        subjects = []
        for seminar in all_seminars:
            if seminar.subject not in subjects:
                ids_to_return.append(seminar.id)
                subjects.append(seminar.subject)

        return Seminar.objects.filter(id__in=ids_to_return)

    @staticmethod
    def get_open_seminars():
        upcoming_seminars = Seminar.objects.filter(date_and_time__gt=timezone.now())
        ids_of_open_seminars = []
        for seminar in upcoming_seminars:
            if not seminar.is_full():
                ids_of_open_seminars.append(seminar.id)

        return Seminar.objects.filter(id__in=ids_of_open_seminars)

    @staticmethod
    def get_closed_seminars():
        upcoming_seminars = Seminar.objects.filter(date_and_time__gt=timezone.now())
        ids_of_closed_seminars = []
        for seminar in upcoming_seminars:
            if seminar.is_full():
                ids_of_closed_seminars.append(seminar.id)

        return Seminar.objects.filter(id__in=ids_of_closed_seminars)

    class Meta:
        ordering = ['subject', 'level']


class Registration(models.Model):
    parent_guardian = models.OneToOneField(Person, models.CASCADE, related_name="parent_guardian")
    parent_guardian_accepts_waiver = models.BooleanField()
    child = models.OneToOneField(Person, models.CASCADE, related_name="child")
    child_accepts_waiver = models.BooleanField()
    registered_seminars = models.ManyToManyField(Seminar)
    additional_info = models.TextField(blank=True, default="")
    time_registered = models.DateTimeField(auto_now_add=True, blank=True, null=False)

    def __str__(self):
        return f"{self.child}"


class Payment(models.Model):
    amount_paid = models.DecimalField(max_digits=8, decimal_places=2)
    registration = models.ForeignKey(Registration, on_delete=models.CASCADE)

    def __str__(self):
        return f"R{self.amount_paid} - {self.registration.parent_guardian} / {self.registration.child}"
