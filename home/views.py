from django.shortcuts import render
from django.db import connection, DatabaseError



def index(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute('SELECT 1')  # Teste de conexão
    except DatabaseError as e:
        return render(request, 'index.html', {'error': 'Erro de conexão com o banco de dados: ' + str(e)})

    return render(request, 'index.html')

