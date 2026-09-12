from rest_framework.routers import DefaultRouter
from .views_api import BookViewSet, CategoryViewSet

router = DefaultRouter()
router.register('books', BookViewSet)
router.register('categories', CategoryViewSet)

urlpatterns = router.urls