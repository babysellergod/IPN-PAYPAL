from flask import Flask, request
import json
import os

app = Flask(__name__)

DB_PATH = "balance.json"

# Si no existe el archivo de saldo, crearlo
if not os.path.exists(DB_PATH):
    with open(DB_PATH, "w") as f:
        json.dump({}, f)

def cargar_saldo():
    with open(DB_PATH, "r") as f:
        return json.load(f)

def guardar_saldo(data):
    with open(DB_PATH, "w") as f:
        json.dump(data, f, indent=4)

@app.route('/')
def index():
    return "✅ Servidor IPN Flask Activo"

@app.route('/ipn', methods=['POST'])
def ipn():
    data = request.form.to_dict()
    print("📥 IPN recibido:", data)

    payer_email = data.get("payer_email")
    amount = float(data.get("mc_gross", 0))

    if payer_email:
        saldo = cargar_saldo()

        # Sumar al saldo de ese correo
        if payer_email not in saldo:
            saldo[payer_email] = 0

        saldo[payer_email] += amount
        guardar_saldo(saldo)

        print(f"💰 Se cargó ${amount:.2f} a {payer_email}")

    return "OK", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Render usa PORT dinámico
    app.run(host="0.0.0.0", port=port)
  
