import oracledb
from flask import Flask, request, jsonify
import traceback
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

# Configurações do banco de dados Oracle
db_username = 'rm551694'
db_password = '061292'
db_dsn = 'oracle.fiap.com.br/orcl'

def get_db_connection():
    return oracledb.connect(
        user=db_username,
        password=db_password,
        dsn=db_dsn
    )

@app.route('/cliente/<int:id>', methods=['GET'])
def get_cliente(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT * FROM cliente WHERE id = :id", id=id)
        cliente = cursor.fetchone()
        if cliente:
            cliente_dict = {
                'id': cliente[0],
                'nome': cliente[1],
                'idade': cliente[2],
                'saldo': float(cliente[3]),
                'data_cadastro': str(cliente[4])
            }
            return jsonify(cliente_dict)
        return jsonify({"message": "Cliente não encontrado!"}), 404
    except oracledb.DatabaseError as error:
        return jsonify({"message": f"Erro ao buscar cliente: {error}"}), 500
    finally:
        cursor.close()
        conn.close()

@app.route('/cliente', methods=['GET'])
def listar_clientes():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT * FROM cliente")
        clientes = cursor.fetchall()
        if clientes:
            clientes_list = [{
                'id': cliente[0],
                'nome': cliente[1],
                'idade': cliente[2],
                'saldo': float(cliente[3]),
                'data_cadastro': str(cliente[4])
            } for cliente in clientes]
            return jsonify(clientes_list)
        return jsonify([])
    except oracledb.DatabaseError as error:
        return jsonify({"message": f"Erro ao listar clientes: {error}"}), 500
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)