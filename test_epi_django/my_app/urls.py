from rest_framework import routers, urlpatterns
from .viewsets import GameViewSet


router = routers.SimpleRouter()
router.register('games', GameViewSet)

app_name = 'my_app'

urlpatterns = router.urls
