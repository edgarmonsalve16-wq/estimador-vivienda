import streamlit as st

st.title("Estimador de Precio de Vivienda 🏠")

m2 = st.number_input("Metros cuadrados:", min_value=10, value=80)
habitaciones = st.selectbox("Habitaciones:", range(1, 6))
baños = st.selectbox("Baños:", range(1, 4))
estrato = st.selectbox("Estrato:", range(1, 7))

if st.button("Estimar precio"):
    precio = 50000000 + (m2 * 800000) + (habitaciones * 10000000) + (baños * 8000000) + (estrato * 5000000)
    st.success(f"💰 Precio estimado: ${precio:,.0f}".replace(",", "."))
