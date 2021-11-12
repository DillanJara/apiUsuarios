from django.db import router
from rest_framework import routers, urlpatterns
from usuarios.viewsets import UsuarioViewset

router = routers.SimpleRouter()
router.register('Usuario', UsuarioViewset)

urlpatterns = router.urls