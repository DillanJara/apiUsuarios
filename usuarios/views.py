from django.shortcuts import redirect, render
from .models import Usuario

# Create your views here.
def principal(request):
    return render(request, 'principal.html')

def guardarUsuario(request):
    varNombre = request.POST.get('usuarioInput') 
    varCorreo = request.POST.get('correoInput')
    varPassword = request.POST.get('claveInput')   
    
    usuario = Usuario()
    usuario.nombreUsuario = varNombre
    usuario.correoUsuario = varCorreo
    usuario.claveUsuario = varPassword

    Usuario.save(usuario)

    return redirect('/')

def listaUsuarios(request):
    return render(request, 'listaUsuarios.html')
