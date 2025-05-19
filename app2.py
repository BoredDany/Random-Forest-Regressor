import json

from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np
from sklearn.decomposition import PCA

app = Flask(__name__)

# Cargar TODOS los modelos pre-entrenados
scaler = joblib.load('minmax_scaler.pkl')
pca = joblib.load('pca_model.pkl')
model = joblib.load('gaussian_pca_model.pkl')
# Definir PCA con los mismos parámetros

pca = PCA(n_components=3)

# Función para cargar las zonas WiFi
def load_wifi_zones():
    with open('static/zonaswifi.json', 'r', encoding='utf-8') as f:
        return json.load(f)

@app.route('/')
def home():
    zonas_wifi = load_wifi_zones()
    return render_template('index2.html', zonas_wifi=zonas_wifi)


@app.route('/predict', methods=['POST'])
def predict():
    try:
        # 1. Obtener datos del formulario
        data = request.form
        input_data = np.array([
            float(data['visitas']),
            float(data['logins']),
            float(data['dispositivos_nuevos']),
        ]).reshape(1, -1)

        # Predecir
        cluster = model.predict(input_data)[0]

        return render_template('index2.html',
                               prediction=cluster,
                               zonas_wifi=load_wifi_zones(),
                               error=None)

    except Exception as e:
        return render_template('index2.html',
                               error=str(e),
                               zonas_wifi=load_wifi_zones(),
                               prediction=None)

if __name__ == '__main__':
    app.run(debug=True)
