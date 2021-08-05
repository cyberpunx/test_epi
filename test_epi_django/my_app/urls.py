from django.urls import path
from . import views
from rest_framework import routers, urlpatterns

router = routers.SimpleRouter()
router.register('games', views.GameViewSet)

app_name = 'my_app'
urlpatterns = [

]

urlpatterns += router.urls
