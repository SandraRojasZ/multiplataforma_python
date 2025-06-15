import firebase_admin
from firebase_admin import credentials, firestore

# Inicializa o Firebase
def init_firebase():
    cred = credentials.Certificate("C:\\Users\\Nome\\multiplataforma\\pasta\\chave.json")
    firebase_admin.initialize_app(cred)
    return firestore.client()

# Chame a função para inicializar o Firebase e obter a instância do banco de dados
db = init_firebase()
