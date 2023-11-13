from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    # Add other student details as needed

class Transaction(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=10, choices=[('income', 'Income'), ('outcome', 'Outcome')])
    date = models.DateField()

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

class Course(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    installment_available = models.BooleanField(default=False)
