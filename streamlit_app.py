import streamlit as st
import requests

ESP_IP = "http://192.168.1.50"  # Ganti dengan IP dari Serial Monitor

st.title("💡 Kontrol LED ESP8266")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Lampu Merah")
    if st.button("ON Merah"):
        r = requests.get(f"{ESP_IP}/led?lamp=merah&state=on")
        st.write("Status:", r.text)
    if st.button("OFF Merah"):
        r = requests.get(f"{ESP_IP}/led?lamp=merah&state=off")
        st.write("Status:", r.text)

with col2:
    st.subheader("Lampu Hijau")
    if st.button("ON Hijau"):
        r = requests.get(f"{ESP_IP}/led?lamp=hijau&state=on")
        st.write("Status:", r.text)
    if st.button("OFF Hijau"):
        r = requests.get(f"{ESP_IP}/led?lamp=hijau&state=off")
        st.write("Status:", r.text)
