from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import BeksarUserManager

class Student(AbstractUser):
    email = models.EmailField(_("email"), unique=True, db_index=True)
    username = None
    phone_number = models.CharField(_("Phone number"), max_length=32, blank=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ("first_name", "last_name")

    objects = BeksarUserManager()

    def __str__(self) -> str:
        return self.get_full_name() or self.email or self.phone_number

class Transaction(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=10, choices=[('income', 'Income'), ('outcome', 'Outcome')])
    date = models.DateField()

    def __str__(self):
        return f"{self.amount} for {self.student}"

class EducationalCredit(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    # Add other credit details as needed

class InstallmentPlan(models.Model):
    educational_credit = models.ForeignKey(EducationalCredit, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()

class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    pub_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class Course(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    installment_available = models.BooleanField(default=False)

    def __str__(self):
        return self.title
