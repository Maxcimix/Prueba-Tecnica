from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__, static_url_path='/static')

def es_numero_perfecto(n):
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
    return jsonify({'numbers': numeros_perfectos})

if __name__ == '__main__':
    app.run(debug=True)


