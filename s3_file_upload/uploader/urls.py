from rest_framework.routers import SimpleRouter
from .views import StoreViewSet, UploadViewSet

router = SimpleRouter()

router.register('upload', UploadViewSet, basename='upload')
router.register('store', StoreViewSet, basename='store')

urlpatterns = []

urlpatterns += router.urls
