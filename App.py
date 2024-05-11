import streamlit as st
from PIL import Image
import requests
from bs4 import BeautifulSoup
import numpy as np
from keras.preprocessing.image import load_img, img_to_array
from keras.models import load_model

model = load_model('IndonesianFoodDaf.h5')

labels = { 0: 'Ikan Gurame Asam Manis' , 1: 'Salmon Panggang' , 2: 'Kari Ayam' , 3: 'Perkedel Jagung' , 4: 'Sandwich Keju' , 5: 'Ikan Bandeng Goreng ' , \
            6: 'Telur Dadar Sayur' , 7: 'Gado-gado' , 8: 'Mie Kocok' , 9: 'Klepon' , 10: 'Cilok' , 11: 'Greek Yoghurt dengan Buah & Granola' , 12: 'Sup Ayam' , \
            13: 'Ayam (Dilapisi Tepung Roti dan Digoreng)' , 14: 'Pempek' , 15: 'Tempe Orek' , 16: 'Kue Apem' , 17: 'Es Krim Strawberry' , 18: 'Mie Ayam' ,\
            19: 'Kerupuk Udang' , 20: 'Kue Bolu Coklat ' , 21: 'Donat (Glazed)' , 22: 'Sup Sayur Ayam' , 23: 'Gelato' , 24: 'Bakso Daging Sapi' ,\
            25: 'Nasi Uduk' , 26: 'Soto Mie' , 27: 'Perkedel Kentang' , 28: 'Telur Goreng' , 29: 'Rawon' , 30: 'Nasi Goreng Ayam' ,\
            31: 'Telur Rebus' , 32: 'Tahu Isi' , 33: 'Kue Lumpur' , 34: 'Kentang Goreng' , 35: 'Nasi Merah' , 36: 'Belgian Waffle' , 37: 'Lasagna' ,\
            38: 'Salad Buah' , 39: 'Siomay' , 40: 'Nasi Goreng' , 41: 'Makaroni Keju' , 42: 'Nasi Padang' , 43: 'Nagasari' , 44: 'Serabi' , 45: 'Martabak Keju' ,\
            46: 'Es Krim Vanila' , 47: 'Rendang' , 48: 'Risol Bihun' , 49: 'Mie Goreng' , 50: 'Soda' , 51: 'Oatmeal Ubi Jalar' , 52: 'Burger' , 53: 'Brownies' , \
            54: 'Tuna Salad Sandwich' , 55: 'Empal Gentong ' , 56: 'Dimsum' , 57: 'Lapis Legit (1 potong)' , 58: 'Tumis Kangkung' , 59: 'Es Krim Coklat' , \
            60: 'Nasi Hainan' , 61: 'Pisang Goreng Madu' , 62: 'Kue Cubit' , 63: 'Ramen Ayam' , 64: 'Spaghetti' , 65: 'Cumi Goreng' , 66: 'Es Kopi' , \
            67: 'Chicken Katsu' , 68: 'Ayam Geprek' , 69: 'Nugget Ayam' , 70: 'Udang Goreng' , 71: 'Keripik Kentang' , 72: 'Risol Mayo' , \
            73: 'Roti Isi Coklat' , 74: 'Es Loli' , 75: 'Bubur Ayam' , 76: 'Mochi' , 77: 'Puding Coklat' , 78: 'Soto Ayam' , 79: 'Bakpia' , \
            80: 'Dadar Gulung (2 lapis)' , 81: 'Sate Ayam' , 82: 'Tumis Tahu' , 83: 'Lumpia Basah' , 84: 'Udang Lapis Tepung' , 85: 'Pecel Lele' , \
            86: 'Pizza Keju' , }

foods = ['Ikan Gurame Asam Manis', 'Salmon Panggang', 'Kari Ayam','Perkedel Jagung', 'Sandwich Keju','Ikan Bandeng Goreng ',\
         'Telur Dadar Sayur','Gado-gado','Mie Kocok','Klepon','Cilok','Greek Yoghurt dengan Buah & Granola','Sup Ayam',\
          'Ayam (Dilapisi Tepung Roti dan Digoreng)', 'Pempek', 'Tempe Orek','Kue Apem','Es Krim Strawberry','Mie Ayam',\
            ]

drinks = ['Beetroot', 'Cabbage', 'Capsicum', 'Carrot', 'Cauliflower', 'Corn', 'Cucumber', 'Eggplant', 'Ginger',
              'Lettuce', 'Onion', 'Peas', 'Potato', 'Raddish', 'Soy Beans', 'Spinach', 'Sweetcorn', 'Sweetpotato',
              'Tomato', 'Turnip']




def prepare_image(img_path):
    img = load_img(img_path, target_size=(224, 224, 3))
    img = img_to_array(img)
    img = img / 255
    img = np.expand_dims(img, [0])
    answer = model.predict(img)
    y_class = answer.argmax(axis=-1)
    print(y_class)
    y = " ".join(str(x) for x in y_class)
    y = int(y)
    res = labels[y]
    print(res)
    return res.capitalize()


def run():
    st.title("Indonesian Foods and Drinks 🍔 🇮🇩 Classification")
    img_file = st.file_uploader("Choose an Image", type=["jpg", "png"])
    if img_file is not None:
        img = Image.open(img_file).resize((250, 250))
        st.image(img, use_column_width=False)
        save_image_path = './upload_images/' + img_file.name
        with open(save_image_path, "wb") as f:
            f.write(img_file.getbuffer())

        # if st.button("Predict"):
        if img_file is not None:
            result = prepare_image(save_image_path)
            if result in foods:
                st.info('**Category : Foods**')
            else:
                st.info('**Category : Drinks**')
            st.success("**Predicted : " + result + '**')


run()