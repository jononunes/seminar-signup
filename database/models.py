from django.db import models
from django.utils import timezone
from django.utils.datetime_safe import datetime


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email_address = models.EmailField(blank=True)
    cellphone_number = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


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

    grade_choices = [
        ("GRADE11", "Grade 11"),
        ("GRADE12", "Grade 12")
    ]
    grade = models.CharField(max_length=10, choices=grade_choices)

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

    def get_one_liner(self):
        return f"{self.get_subject_display()} [{datetime.strftime(self.date_and_time, '%a %d %b - %H:%M')}]"

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
    def get_upcoming_seminars():
        return Seminar.objects.filter(date_and_time__gt=timezone.now())

    @staticmethod
    def get_open_seminars():
        upcoming_seminars = Seminar.get_upcoming_seminars()
        ids_of_open_seminars = []
        for seminar in upcoming_seminars:
            if not seminar.is_full():
                ids_of_open_seminars.append(seminar.id)

        return Seminar.objects.filter(id__in=ids_of_open_seminars)

    @staticmethod
    def get_closed_seminars():
        upcoming_seminars = Seminar.get_upcoming_seminars()
        ids_of_closed_seminars = []
        for seminar in upcoming_seminars:
            if seminar.is_full():
                ids_of_closed_seminars.append(seminar.id)

        return Seminar.objects.filter(id__in=ids_of_closed_seminars)

    class Meta:
        ordering = ['date_and_time']


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
    m_payment_id = models.CharField(max_length=100)
    pf_payment_id = models.IntegerField()
    payment_status = models.CharField(max_length=100)
    item_name = models.CharField(max_length=100)
    amount_gross = models.DecimalField(max_digits=10, decimal_places=2)
    amount_fee = models.DecimalField(max_digits=10, decimal_places=2)
    amount_net = models.DecimalField(max_digits=10, decimal_places=2)
    registration = models.ForeignKey(Registration, on_delete=models.CASCADE)

    def __str__(self):
        return f"R{self.amount_gross} - {self.registration.parent_guardian} / {self.registration.child}"


class NotificationError(models.Model):
    error_description = models.TextField(blank=True)
    notification_post_info = models.TextField(blank=True)
    time_registered = models.DateTimeField(auto_now_add=True, blank=True, null=False)

    def __str__(self):
        return str(self.time_registered)


class Package(models.Model):
    name = models.CharField(max_length=40)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    seminars = models.ManyToManyField(Seminar)

    def __str__(self):
        return self.name

    def get_price(self):
        price = float(sum([s.base_price for s in self.seminars.all()])) * (1.0 - float(self.discount / 100))
        return f"{price:.2f}"

    def get_seminars_per_line(self):
        return [s.get_one_liner() for s in self.seminars.all()]

    def get_fancy_name(self):
        grade = [s.get_grade_display() for s in self.seminars.all()][0]
        return f"{grade} {self.name}"

    def get_seminar_ids(self):
        return ",".join([str(s.id) for s in self.seminars.all()])
