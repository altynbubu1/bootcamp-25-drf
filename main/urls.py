from rest_framework.routers import SimpleRouter

from main.views import PersonViewSet, ContactViewSet

router = SimpleRouter()
router.register('person', PersonViewSet, basename='person')
router.register('contact', ContactViewSet, basename='contact')

urlpatterns = router.urls