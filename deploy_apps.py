import pickle
import streamlit as st

# Muat model yang telah disimpan
model_analisis = pickle.load(open('tweettayangantv_sentimen.pkl', 'rb'))

# Membuat aplikasi Streamlit
st.title("Analisis Tayangan TV")

clean_teks = st.text_input("Masukkan teks yang ingin dianalisis")
analisis_detection = ''

if st.button('Hasil Analisis'):
    # Prediksi menggunakan model yang telah dilatih
    predict_pipeline = model_analisis.predict([clean_teks])

    if predict_pipeline[0] == 'positive':  # Misalkan 'positive' adalah label positif
        analisis_detection = "review positif"
    else:
        analisis_detection = "review negatif"

st.success(analisis_detection)
