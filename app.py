from flask import Flask, render_template, request, jsonify
import pyodbc 
from datetime import datetime
import math

app = Flask(__name__, static_url_path='/static')

server= 'MAXCIMIX'
database='Pruebatecnica'
user='sa'
password='123'
connection = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+user+';PWD='+password)

def es_numero_perfecto(n):
    if n % 2 != 0:
        return False  # No se puede obtener un número perfecto para números impares excepto para 1
    suma = sum(divisor + n // divisor for divisor in range(2, int(math.sqrt(n)) + 1) if n % divisor == 0)
    return suma + 1 == n
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/find-perfect-numbers')
def find_perfect_numbers():
    start = int(request.args.get('start'))
    end = int(request.args.get('end'))
    numeros_perfectos = [num for num in range(start, end + 1) if es_numero_perfecto(num)]
    # Insertar los números perfectos en la base de datos
    data = connection.cursor()
    # Crear una cadena separada por comas de los números perfectos encontrados
    numeros_str = ', '.join(map(str, numeros_perfectos))
    # Insertar una sola fila con los números perfectos encontrados
    fecha = datetime.now()
    data.execute('''
        INSERT INTO Result (inicio_rango, final_rango, resultado, fecha)
        VALUES (?, ?, ?, ?)
    ''', (start, end, numeros_str, fecha))
    connection.commit()
    data.close()

    return jsonify({'numbers': numeros_perfectos})


if __name__ == '__main__':
    app.run(port=3000,debug=True)


