import streamlit as st
from openai import OpenAI



client = OpenAI()

txtobj = st.text("Chargement en cours...")
    
completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user","content": "write a haiku about ai"}
    ]
)

txtobj.text(completion.choices[0].message.content)

# import streamlit as st

# Texte
# st.write("Write")
# st.text("Text")
# st.header("Header")
# st.subheader("Subheader")

# # Input
# st.button("Button")
# st.checkbox("Checkbox")
# st.toggle("Toggle")
# st.radio("Radio", ["Première option", "Seconde option"])
# st.text_input("Text Input")
# st.audio_input("Audio Input")
# st.file_uploader("File Uploader")
# st.slider("Slider", 0, 100)

# # Navigation
# pg = st.navigation([
#     st.Page("page1.py", title="First page", icon="🔥"),
#     st.Page("page2.py", title="Second page", icon="😊"),
# ])
# pg.run()

# # Media
# st.image("image.webp", width=50, caption="Image")
# st.audio("audio.wav")