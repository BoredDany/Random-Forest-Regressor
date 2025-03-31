<h1 align="center">
  Random-Forest-Regressor  
</h1>
Este proyecto implementa un modelo de Machine Learning (Random Forest) para predecir métricas clave de comportamiento digital basado en una base de datos.

* ****
* **Base de Datos Utilizada:**
* * https://www.datos.gov.co/Ciencia-Tecnolog-a-e-Innovaci-n/Uso-de-Zonas-Wifi-Cartagena-de-Indias/xpqd-7i9w
  * Esta base de datos registra el uso diario de zonas WiFi públicas en bibliotecas y espacios comunitarios de Cartagena , incluyendo métricas como visitas (dispositivos únicos conectados), logins (accesos autenticados), dispositivos nuevos (primeras conexiones), sesiones (interacciones con la red) y consumidores (usuarios activos). Los datos nos permitieron generar el modelo utilizado en la pagina web.

* ****
* ****
* **Análisis y Modelo Generados:**
* * https://colab.research.google.com/drive/1ZaOW5zWFSRCkZWoon4RXxc2i3PkqDNyU?usp=sharing
* **Metodología:**
  * Se evaluaron tres modelos predictivos (Árbol de Decisión, Red Neuronal y Random Forest) para predecir consumidores WiFi
  * El Random Forest mostró el mejor desempeño con RMSE de 5.21 en datos de prueba
  * El modelo final fue seleccionado por su balance entre precisión y capacidad de generalización
  * Se conservaron outliers detectados al no afectar significativamente el desempeño del modelo
* **Implementación:**
  * Variables clave: Visitas, Logins, Dispositivos Nuevos, Sesiones y Zona WiFi
  * Hiperparámetros optimizados mediante RandomizedSearchCV
  * Arquitectura final con 200 árboles y profundidad máxima de 20 nodos
* **Resultados:**
  * Error promedio de predicción: ±5 consumidores
  * Buen equilibrio entre datos de entrenamiento (RMSE 2.17) y prueba (RMSE 5.21)
  * Modelo exportado como `random_forest_model.pkl` para integración
* ****

<h2 align="center">
  Ejecución
</h2>

## Importación
Dirijase a su terminal dentro del proyecto e instale estas librerias:
```bash
pip install flask
pip install joblib
pip install numpy
pip install scikit-learn
```

## Compilación
En la terminal, diríjase al directorio del proyecto y ejecute el comando:
```bash
python app.py
```
Depues dirijase a la url que le asigna flusk.


## :man: Autores
**Daniela Martinez**

**Isabella Rodriguez**

**Jose Jaramillo**

**David Parra**
