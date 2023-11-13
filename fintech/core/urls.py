from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    StudentViewSet,
    TransactionViewSet,
    EducationalCreditViewSet,
    InstallmentPlanViewSet,
    NewsViewSet,
    CourseViewSet,
)

router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'transactions', TransactionViewSet)
router.register(r'educational-credits', EducationalCreditViewSet)
router.register(r'installment-plans', InstallmentPlanViewSet)
router.register(r'news', NewsViewSet)
router.register(r'courses', CourseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
