from rest_framework.routers import DefaultRouter

from .views import DoctorViewSet, DiseaseViewSet

router = DefaultRouter()

router.register(r'doctors', DoctorViewSet)
router.register(r'diseases', DiseaseViewSet)

urlpatterns = router.urls

