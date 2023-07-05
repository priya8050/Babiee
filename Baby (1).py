#!/usr/bin/env python
# coding: utf-8

# In[40]:



import streamlit as st
from PIL import Image

def Pyaar():
    st.title('Sallu and uski biwi Ke love estory')
    st.button('My bubbu')

    # Add your Pyaar page content here
    image = Image.open('C:/Users/admin/Downloads/20230107_162336-PHOTO_FRAME.jpg')
    st.image(image, caption='How lucky are you ?', use_column_width=True)

def Prema():
    st.title('Beginning')
    with st.expander("Touch me !! ummmah"):
        st.write("It all started back then in 1947, in that dreamgains, I gained you")
        st.write("Pyaar Ka Ye Ehsaas Pyaar Se Bhi Pyara Hai, Dekhiye Ji Pyaar Mera Pyaar Se Bhi Pyaara Hai, Na Raha Koi Kaabu Is Par Na Koi Sahaara Hai, Dil jaan Aur Jigar, Ye Sab Kuch To Tumhara Hai")
        st.checkbox('You have no choice of leaving me, so click, I agree')

    # Add your Prema page content here
    image = Image.open('C:/Users/admin/Downloads/IMG-20211006-WA0001.jpg')
    st.image(image, caption='Congratulations, you found your bubu, there\'s no going back')

def ISHQ():
    st.title("You are my honey bunch")
    st.subheader('I LOVE YOU')
    image = Image.open('C:/Users/admin/Downloads/IMG20211113172327.jpg')
    st.image(image, caption='Laddu <3')
    ia = st.radio('what\'s forever??', ["I 4 U", "U 4 ME"])
    st.write("You selected:", ia)

    # Add your ISHQ page content here
    image = Image.open('C:/Users/admin/Downloads/IMG_20221018_175729.jpg')
    st.image(image, caption='Miyyaaa <3')

def FOREVER():
    st.title('QUBHOOL HAI')
    st.header('YOU AND ME ITS A FOREVER KINDA THING <3')
    with st.expander("Touch me !! AGAIN"):
        st.write("Kitna pyar hai tumse yeh jan lo, Tum hi zindagi ho meri Is baat ko maan lo,")
        st.write("Tumhe dene ko mere paas Kuchh bhi nahi, Bas ek jaan hai Jab ji chahe maang lo..")

    # Add your Forever page content here
    image = Image.open('C:/Users/admin/Downloads/IMG20220424224652.jpg')
    st.image(image, caption='Miyyaaa <3')


# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ("Pyaar", "Prema", "ISHQ", "Forever"))

# Render selected page
if page == "Pyaar":
    Pyaar()
elif page == "Prema":
    Prema()
elif page == "ISHQ":
    ISHQ()
elif page == "Forever":
    FOREVER()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




