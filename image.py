import streamlit as st
from PIL import Image

def main():
    st.title("Font Style Changer")
    st.write("Upload an image and change the font style of the extracted text!")

    uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        
        st.subheader("Enter Your Text:")
        user_text = st.text_area("Type something here...")
        
        st.subheader("Select a Font Style")
        font_style = st.selectbox("Choose a font", ["Arial", "Times New Roman", "Courier New", "Comic Sans MS"])
        
        if user_text:
            st.markdown(f"<p style='font-family:{font_style}; font-size:20px;'>{user_text}</p>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
