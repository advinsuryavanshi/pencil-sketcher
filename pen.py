import streamlit as st
import numpy as np
from PIL import Image
import cv2 

st.set_page_config(page_title = "Pencil Sketcher ", page_icon = ":wink:", layout = "wide")

def penSk(inp_img):
    img_gray = cv2.cvtColor(inp_img, cv2.COLOR_BGR2GRAY)
    img_invert = cv2.bitwise_not(img_gray)
    img_smoothing = cv2.GaussianBlur(img_invert, (21, 21),sigmaX=0, sigmaY=0)
    final_img = dodgeV2(img_gray, img_smoothing)
    return(final_img)

def dodgeV2(x, y):
    return cv2.divide(x, 255 - y, scale=256)


st.title("Pencil Sketcher App")
st.write("This app can make a pencil sketch of your photo")

file_image = st.sidebar.file_uploader("Upload your photo", type=['jpeg',"png","jpg"])

if file_image is None:
    st.write("You haven't uploaded any image file")
else:
    input_img = Image.open(file_image)
    final_img = penSk(np.array(input_img))


    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.subheader("Input Photo")
            st.image(file_image)
        with right_column:
            st.subheader("Output Pencil Sketch")
            st.image(final_img)

            
