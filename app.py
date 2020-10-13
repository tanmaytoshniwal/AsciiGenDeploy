import streamlit as st
from PIL import Image, ImageDraw
import math

st.title("ASCII GENERATOR")

chars="`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

charArr=list(chars)
charLength=len(charArr)
interval=charLength/256

scalefactor=0.8

oneCharWidth=8
oneCharHeight=18

def getChar(intInput):
    return charArr[math.floor(intInput*interval)]

converted_file=open('Output.txt','w')
im = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

def convert(im):
    width, height=im.size

    im=im.resize((int(scalefactor*width), int(scalefactor*height*(oneCharWidth/oneCharHeight))),Image.NEAREST)
    width, height=im.size
    pix=im.load()

    OutputImage=Image.new('RGB',(oneCharWidth*width,oneCharHeight*height),color=(0,0,0))
    d=ImageDraw.Draw(OutputImage)

    for i in range(height):
        for j in range(width):
            r,g,b=pix[j,i]
            h=int(r/3+g/3+b/3)
            pix[j,i]=(h, h, h)
            converted_file.write(getChar(h))
            d.text((j*oneCharWidth,i*oneCharHeight),getChar(h),fill=(r,g,b))
        converted_file.write('\n')

    #OutputImage.save('output.png')
    #st.image("output.png", use_column_width=True)
    st.image(OutputImage, use_column_width=True)
    return OutputImage
    #return 'output.png'
    #return st.image("output.png", output_format="PNG")

import os
import base64
def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">Download {file_label}</a>'
    return href



if im is None:
    st.text("Please upload an image file")
else:
    image = Image.open(im)
    st.image(image, use_column_width=True)
    result=convert(image)
    st.markdown(get_binary_file_downloader_html(result, 'Picture'), unsafe_allow_html=True)
