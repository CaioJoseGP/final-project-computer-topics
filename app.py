import os
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

DB_HOST = os.environ.get('DB_HOST', 'localhost')
DB_USER = os.environ.get('DB_USER', 'admin')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'adminpassword')
DB_NAME = os.environ.get('DB_NAME', 'admissoes')

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelo de Dados
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200))
    city = db.Column(db.String(100))
    state = db.Column(db.String(50))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(20))

with app.app_context():
    db.create_all()

# --- Algoritmo de Estresse de CPU ---
def cpu_stress_hanoi(n, source, destination, auxiliary):
    """
    Resolve a Torre de Hanói. Com n=22, gera mais de 4 milhões de chamadas recursivas,
    segurando a CPU por alguns segundos para simular a lentidão relatada.
    """
    if n == 1:
        return
    cpu_stress_hanoi(n-1, source, auxiliary, destination)
    cpu_stress_hanoi(n-1, auxiliary, destination, source)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/students', methods=['GET'])
def get_students():
    cpu_stress_hanoi(28, 'A', 'C', 'B') 
    
    students = Student.query.all()
    result = []
    for s in students:
        result.append({
            'id': s.id, 'name': s.name, 'address': s.address,
            'city': s.city, 'state': s.state, 'email': s.email, 'phone': s.phone
        })
    return jsonify(result)

@app.route('/api/students', methods=['POST'])
def add_student():
    data = request.json
    new_student = Student(
        name=data['name'], address=data.get('address', ''),
        city=data.get('city', ''), state=data.get('state', ''),
        email=data.get('email', ''), phone=data.get('phone', '')
    )
    db.session.add(new_student)
    db.session.commit()
    return jsonify({'message': 'Aluno adicionado com sucesso!'}), 201

@app.route('/api/students/<int:id>', methods=['PUT'])
def update_student(id):
    data = request.json
    student = Student.query.get_or_404(id)
    
    student.name = data.get('name', student.name)
    student.address = data.get('address', student.address)
    student.city = data.get('city', student.city)
    student.state = data.get('state', student.state)
    student.email = data.get('email', student.email)
    student.phone = data.get('phone', student.phone)
    
    db.session.commit()
    return jsonify({'message': 'Aluno atualizado com sucesso!'})

@app.route('/api/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    return jsonify({'message': 'Aluno excluído com sucesso!'})

if __name__ == '__main__':
    # Roda em todas as interfaces de rede na porta 5000
    app.run(host='0.0.0.0', port=5000)
