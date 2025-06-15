from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/ipn', methods=['POST'])
def ipn_listener():
    data = request.form.to_dict()
    print("📥 IPN recibido:", data)
    # Aquí puedes validar con PayPal, guardar en DB, o enviar notificación
    return "OK", 200

@app.route('/')
def index():
    return "Servidor Flask IPN activo"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
  
