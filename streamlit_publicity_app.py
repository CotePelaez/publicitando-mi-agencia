import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

st.markdown("""
    <style>
    .stButton button {
        background-color: #89adb5   ;
        color: white;
        font-size: 34px;
        height: 50px;
        width: 140px;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# Función para enviar correo
def send_email(subject, message, recipient_email):
    sender_email = "mpelaezmath@gmail.com"  # Cambia esto a tu correo
    sender_password = "your_email_password"  # Cambia esto a tu contraseña

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = recipient_email
    msg["Subject"] = subject

    msg.attach(MIMEText(message, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
        server.close()
        return True
    except Exception as e:
        print(f"Error al enviar el correo: {e}")
        return False

# Datos de los viajes con imágenes reales
trips = [
    {
        "name": "Viaje a Nepal",
        "description": "Un emocionante viaje a las montañas con vistas espectaculares.",
        "image": "nepal.jpeg",
    },
    {
        "name": "Aventura en Bangladesh",
        "description": "Disfruta de las mejores playas en un viaje inolvidable.",
        "image": "bangladesh.jpeg",
    },
    {
        "name": "Escapada a Venezuela",
        "description": "Explora la vibrante vida de la ciudad con todas sus comodidades.",
        "image": "venezuela.jpeg",
    },
    {
        "name": "Eritrea, un tesoro",
        "description": "Una experiencia única para ver la vida africana de cerca.",
        "image": "eritrea.jpeg",
    },
    {
        "name": "Iran, un secreto",
        "description": "Sumérgete en la cultura local y aprende sobre su historia.",
        "image": "iran.jpeg",
    },
    {
        "name": "Pakistan: dejate sorprender",
        "description": "Sumérgete en un viaje inesperado.",
        "image": "pakistan.jpeg",
    },
]

st.title("Bienvenido a nuestra Agencia de Viajes")
st.write("Explora nuestros emocionantes viajes y elige el que máste guste.")

# Mostrar los viajes en filas de dos columnas
for i in range(0, len(trips), 2):
    cols = st.columns(2)
    
    for j in range(2):
        if i + j < len(trips):
            with cols[j]:
                st.image(trips[i + j]["image"], use_column_width=True)
                st.subheader(trips[i + j]["name"])
                st.write(trips[i + j]["description"])
                if st.button(f"Estoy interesado", key=f"btn_{i+j}"):
                    if send_email(
                        subject=f"Interés en {trips[i + j]['name']}",
                        message=f"Estoy interesado en el {trips[i + j]['name']}.",
                        recipient_email="mpelaezmath@gmail.com",  # Cambia esto a tu correo
                    ):
                        st.success("¡Correo enviado con éxito!")
                    else:
                        st.error("Hubo un problema al enviar el correo.")
