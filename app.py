import json

from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Cargar el modelo entrenado
model = joblib.load('random_forest_model.pkl')
def load_wifi_zones():
    with open('static/zonaswifi.json', 'r', encoding='utf-8') as f:
        return json.load(f)

@app.route('/')
def home():
    zonas_wifi = load_wifi_zones()
    return render_template('index.html', zonas_wifi=zonas_wifi)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Obtener datos del formulario
        data = request.form
        input_data = np.array([
            float(data['visitas']),
            float(data['logins']),
            float(data['dispositivos_nuevos']),
            float(data['sesiones']),
            float(data['zona_wifi'])
        ]).reshape(1, -1)

        # Hacer la predicción
        prediction = model.predict(input_data)[0]

        # Cargar las zonas WiFi nuevamente
        zonas_wifi = load_wifi_zones()

        return render_template('index.html',
                               prediction=prediction,
                               zonas_wifi=zonas_wifi,
                               error=None)

    except Exception as e:
        # Cargar las zonas WiFi incluso en caso de error
        zonas_wifi = load_wifi_zones()
        return render_template('index.html',
                               error=str(e),
                               zonas_wifi=zonas_wifi,
                               prediction=None)

if __name__ == '__main__':
    app.run(debug=True)
