from rest_framework.routers import SimpleRouter
from .views import UploadViewSet

router = SimpleRouter()

router.register('upload', UploadViewSet, basename='upload')

urlpatterns = []

urlpatterns += router.urls
