import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
st.title("PRIMER TITULO CREADO")
st.write("Primer texto creado en Streamlit, me gusta [Link 22,200 monedas] (https://www.youtube.com/watch?v=LdystjGNEaY)")

Cantidad=st.slider("Selecciona la cantidad")

st.write(f"la cantidad seleccionada es {Cantidad}")

st.button("Primer Boton")

for i in range(0, Cantidad):
    st.button(f"{i}")
