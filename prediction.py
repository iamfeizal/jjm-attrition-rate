from tensorflow.keras.models import load_model
from sklearn.preprocessing import StandardScaler

import pickle
import numpy as np

# Memuat model dari folder SavedModel
model_path = "./jjm_model"  # Atau "attrition_model" jika format SavedModel digunakan
model = load_model(model_path)
print("Model loaded successfully.")

# Load scaler
with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)
print("Scaler loaded successfully.")

# masukkan data dengan urutan 'Age', 'EnvironmentSatisfaction', 'JobInvolvement', 'JobLevel', 'MaritalStatus', 'MonthlyIncome', 'OverTime', 'StockOptionLevel', 'TotalWorkingYears', 'YearsAtCompany', 'YearsInCurrentRole', 'YearsWithCurrManager'.

input_data = np.array([36, 2, 3, 1, 2, 2153, 0, 0, 8, 8, 1, 7])
input_data = scaler.transform([input_data])

# Lakukan prediksi menggunakan model
predictions = model.predict(input_data)
predicted_classes = (predictions > 0.5).astype(int)

# **4. Display Results**
for i, pred in enumerate(predicted_classes):
    result = "Attrition (1=True)" if pred[0] == 1 else "No Attrition (0=False)"
    print(f"Sample {i+1}: Predicted = {result}, Probability = {predictions[i][0]:.2f}")