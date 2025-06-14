from flask import Flask, request, jsonify, render_template
import firebase_admin
from firebase_admin import credentials, firestore

# Inicializa o aplicativo Flask
app = Flask(__name__)

cred = credentials.Certificate("./firebase-auth.json")
firebase_admin.initialize_app(cred)

# Chame a função para inicializar o Firebase e obter a instância do banco de dados
db = firestore.client()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/create', methods=['POST'])
def create():
    data = request.json  # Obtém os dados do JSON enviado
    if data:    
        doc_ref = db.collection('tb_cliente').add(data)
        print(doc_ref)
        return jsonify({"status": "Cliente adicionado", "document_id": doc_ref[1].id}), 201
    else:
        return jsonify({"erro": "Informação não fornecida"}), 400

# 📥 READ - Lista todos os clientes
@app.route('/read/<document_id>', methods=['GET'])
def read(document_id):
    doc_ref = db.collection('tb_cliente').document(document_id)
    doc = doc_ref.get()
    if doc.exists:                
        return jsonify(doc.to_dict()), 200
    else:
        return jsonify({'erro': "Documento não encontrado"}), 404

# UPDATE - Atualiza cliente por ID
@app.route('/update/<document_id>', methods=['PUT'])
def update(document_id):
    data = request.json
    if data:
        db.collection('tb_cliente').document(document_id).update(data)
        return jsonify({'status': "Cliente atualizado"}), 200
    else:
        return jsonify({"status": "Nenhum dado fornecido"}), 400

# DELETE - Remove cliente por ID
@app.route('/delete/<document_id>', methods=['DELETE'])
def delete(document_id):
    db.collection('tb_cliente').document(document_id).delete()   
    return jsonify({"status": "Cliente removido"}), 200

# Direciona para a página
@app.route('/lista')
def lista():
    return render_template('lista.html')

# Direciona para a página
@app.route('/clientes', methods=['GET'])
def get_clientes():
    docs = db.collection('tb_cliente').stream()
    clientes = [{**doc.to_dict(), 'id': doc.id} for doc in docs]
    return jsonify(clientes)

# Direciona para a página atualiza
@app.route('/atualiza/<document_id>')
def atualiza(document_id):
    return render_template('atualiza.html', document_id=document_id)
   

if __name__ == '__main__':
    app.run(debug=True)
