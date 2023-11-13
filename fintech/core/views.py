from rest_framework import viewsets
from .models import Student, Transaction, EducationalCredit, InstallmentPlan, News, Course
from .serializers import StudentSerializer, TransactionSerializer, EducationalCreditSerializer, InstallmentPlanSerializer, NewsSerializer, CourseSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class EducationalCreditViewSet(viewsets.ModelViewSet):
    queryset = EducationalCredit.objects.all()
    serializer_class = EducationalCreditSerializer

class InstallmentPlanViewSet(viewsets.ModelViewSet):
    queryset = InstallmentPlan.objects.all()
    serializer_class = InstallmentPlanSerializer

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
