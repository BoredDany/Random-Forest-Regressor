from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Cargar el modelo entrenado
model = joblib.load('random_forest_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

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

        return render_template('index.html', prediction=prediction)

    except Exception as e:
        return render_template('index.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)
