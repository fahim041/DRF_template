from rest_framework.routers import SimpleRouter
from .views import FileViewSet, StoreViewSet, UploadViewSet

router = SimpleRouter()

router.register('upload', UploadViewSet, basename='upload')
router.register('store', StoreViewSet, basename='store')
router.register('file', FileViewSet, basename='file')

urlpatterns = []

urlpatterns += router.urls
