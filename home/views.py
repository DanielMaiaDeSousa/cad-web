from django.shortcuts import render
from django.db import connection, DatabaseError
from .models import *


def index(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute('SELECT 1')  # Teste de conexão
    except DatabaseError as e:
        return render(request, 'index.html', {'error': 'Erro de conexão com o banco de dados: ' + str(e)})

    return render(request, 'index.html')

def categoria(request):
    contexto = {
        'lista': Categoria.objects.all().order_by('-id'),
    }
    return render(request, 'categoria/lista.html',contexto)


