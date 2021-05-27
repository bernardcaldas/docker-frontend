import streamlit as st 
from PIL import Image


def main():
    st.title('WebApp runing in docker image')
    st.subheader('Hello World - running webapp streamlit ')
    image_file = st.file_uploader('Upload your image', type=['jpg', 'png', 'jpeg'])

    if image_file is not None:
        ourimage = Image.open(image_file)
        st.text('uploaded file')
        st.image(ourimage)



if __name__ == '__main__':
    main()