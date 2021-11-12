from usuarios.models import Usuario
from rest_framework import viewsets
from usuarios.serializer import UsuarioSerializer

class UsuarioViewset(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer