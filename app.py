import streamlit as st
from PIL import Image
from kanji_helpers import (
    extract_kanji_from_image,
    get_readings,
    create_quiz_from_readings
)

st.title("🌸 Smart Kanji Learning App 🌸")

uploaded = st.file_uploader("Upload an image with Kanji", type=["jpg","png","jpeg"])
if uploaded:
    # Save temp file
    img_path = "temp.jpg"
    with open(img_path, "wb") as f:
        f.write(uploaded.getbuffer())

    # OCR
    kanji_text = extract_kanji_from_image(img_path)
    st.subheader("Extracted Kanji Text")
    st.write(kanji_text)

    # Readings
    readings = get_readings(kanji_text)
    st.subheader("Token Readings")
    for r in readings:
        st.write(f"{r['surface']} → {r['reading']}")

    # Quiz
    quiz = create_quiz_from_readings(readings)
    st.subheader("Quiz Time!")
    st.write(quiz['question'])
    choice = st.radio("Options", quiz['options'])
    if st.button("Submit"):
        if choice == quiz['answer']:
            st.success("Correct! 🎉")
        else:
            st.error(f"Oops… correct was: {quiz['answer']}")
