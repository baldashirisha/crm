from app.api.views import UserViewSet, ContactViewSet, NotesViewSet
from rest_framework.routers import DefaultRouter

router =  DefaultRouter()
router.register(r'', UserViewSet, basename='api')
router.register(r'contact', ContactViewSet, basename='api')
router.register(r'notes', NotesViewSet, basename='api')
urlpatterns = router.urls