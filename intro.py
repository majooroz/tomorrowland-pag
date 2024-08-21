import streamlit as st
from PIL import Image
st.title("😎 MI PRIMERA APP 😎")
st.header("Aqui subire todo el contenido")
st.write("Hola mi gente el dia de hoy hablaremos de Tomorrowlnad")
image = Image.open("mclaren.jpg")
st.image(image,caption = "mclaren")
texto = st.text_input('Aviso parroquial',"Tienes 20 años y no has conseguido un carro deportivo, pues que lastima yo tampoco")
st.write("El texto escrito es", texto)

st.subheader("Vamos a probar dos columnas")
col1, col2 = st.columns(2)

with col1:
  st.subheader("Primera columna")
  st.write("Que es una interfaz?")
  resp = st.checkbox("Preguntele a chatgpt")
  if resp:
    st.write("Preste atención a la clase")

with col2:
  st.subheader("Segunda columna")
  modo = st.radio("Selecciona las marcas que te gustaría comprar", ("Chevrolet", "Renault","Ford"))
  if modo == "Chevrolet":
    st.write("Es una marca interesante")
  if modo == "Renault":
    st.write("Es una marca francesa")
  if modo == "Ford":
    st.write("La marca mas vendida en los estados unidos")

with st.sidebar:
  st.subheader("Decidete de una vez 🛒")
  mod_radio = st.radio(
    "Escoge una marca", 
    ("Chevrolet", "Renault","Ford")
  )
