import streamlit as st
from PIL import Image
st.markdown("""
    <style>
    .title {
        font-family: 'Arial', sans-serif;
        color: #2E86C1;
    }
    .header {
        font-family: 'Courier New', Courier, monospace;
        color: #D35400;
    }
    .content {
        font-family: 'Verdana', sans-serif;
        color: #1ABC9C;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<h1 class="title">THE BEST FESTIVAL IN THE WORLD</h1>', unsafe_allow_html=True)
st.markdown('<h2 class="header">Aqui subire todo el contenido</h2>', unsafe_allow_html=True)
st.markdown('<p class="content">Hola mi gente, el día de hoy hablaremos de Tomorrowland</p>', unsafe_allow_html=True)



image = Image.open("tomorrowland.jpg")
st.image(image,caption = "tomorrowland")
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
  modo = st.radio("Selecciona los festiavles a los que quisieras ir ", ("Ultra", "Renault","Ford"))
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
