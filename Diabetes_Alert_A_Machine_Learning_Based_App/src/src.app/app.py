import gradio as gr
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler
from xgboost import XGBClassifier

# Carregar o modelo e o scaler salvos
with open('xgboost_model.pkl', 'rb') as model_file, open('scaler.pkl', 'rb') as scaler_file:
    model = pickle.load(model_file)
    scaler = pickle.load(scaler_file)

# Definir o limiar de classificação
threshold = 0.7

# Função para prever o diabetes com tratamento de erros


def predict_diabetes(pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age):
    try:
        # Criar o DataFrame com os valores de entrada
        input_data = pd.DataFrame([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age]],
                                  columns=['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age'])

        # Escalar os dados de entrada
        input_data_scaled = scaler.transform(input_data)

        # Prever a probabilidade de diabetes
        prediction_prob = model.predict_proba(input_data_scaled)[:, 1]

        # Aplicar o limiar de classificação
        prediction = (prediction_prob >= threshold).astype(int)

        return 'Diabetes Risk: Positive' if prediction[0] == 1 else 'Diabetes Risk: Negative'
    except Exception as e:
        return f'An error occurred: {str(e)}'


# Create the Gradio interface
iface = gr.Interface(
    fn=predict_diabetes,
    inputs=[
        gr.Number(label='Pregnancies', value=0),
        gr.Slider(minimum=0, maximum=300,
                  label='Glucose (Postprandial Glucose (Normal: Less than 140, Pre-diabetes: Between 140 and 199, Diabetes: 200 or more))', value=150),
        gr.Slider(minimum=0, maximum=200, label='Blood Pressure (Low pressure (It may be normal for some people to have less than 60) Normal: 60 to 80, High Pressure: 90)', value=89),
        gr.Slider(minimum=0, maximum=100,
                  label='Skin Thickness (Typically varies from 10 to 50 mm, but can depend on factors such as age and gender)', value=51),
        gr.Slider(minimum=0, maximum=800,
                  label='Insulin (Normal= 16 to 166 μU/mL)', value=167),
        gr.Slider(minimum=0, maximum=67,
                  label='BMI (Normal= 18.5 to 24.9)', value=24.9),
        gr.Slider(minimum=0, maximum=2.5, step=0.1,
                  label='Diabetes Pedigree Function (Genetic probability, the higher the value, the greater the risk: Above 0.3 based on (this model has risk))', value=0.2),
        gr.Number(minimum=21, maximum=90, label='Age', value=30)
    ],
    outputs='text',
    title='Diabetes Prediction App',
    description="Select the required features to predict the risk of diabetes. Note: The descriptions for each option are purely informative, as each feature will vary in relation to others based on the created model.",
)


# Salvar o scaler em um arquivo pickle após o ajuste
with open('scaler.pkl', 'wb') as scaler_file:
    pickle.dump(scaler, scaler_file)

# Lançar o aplicativo
iface.launch()
