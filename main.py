from flask inport Flask, request, jsonfy

app = Flask(__name__)

#Crear la ruta del endpoint
@app.route('/notificar', methods=['POST'])
def notificar():
    data=request.json
    nombre = data.get("nombre", "desconocido")
    print(f" Notificando a {nombre}...")
    return jsonfy({"notificacion": f"Se notificó a {nombre} exitosamente."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', por =10000)