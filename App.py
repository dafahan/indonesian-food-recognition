import streamlit as st
from PIL import Image
import requests
from bs4 import BeautifulSoup
import numpy as np
from keras.preprocessing.image import load_img, img_to_array
from keras.models import load_model

model = load_model('IndonesianFoodDaf.h5')

labels = {0: 'Air Putih', 1: 'Ayam (Dilapisi Tepung Roti dan Digoreng)', 2: 'Ayam Geprek', 3: 'Bakpia', 4: 'Bakso Daging Sapi', 5: 'Belgian Waffle', 6: 'Brownies', 7: 'Bubur Ayam', 8: 'Burger', 9: 'Cappucino', 10: 'Cendol', 11: 'Chicken Katsu', 12: 'Cilok', 13: 'Cumi Goreng', 14: 'Dadar Gulung (2 lapis)', 15: 'Dimsum', 16: 'Donat (Glazed)', 17: 'Empal Gentong', 18: 'Es Campur', 19: 'Es Dawet', 20: 'Es Doger', 21: 'Es Jeruk Peras', 22: 'Es Kacang Merah', 23: 'Es Kelapa Muda', 24: 'Es Kopi', 25: 'Es Krim Coklat', 26: 'Es Krim Strawberry', 27: 'Es Krim Vanila', 28: 'Es Loli', 29: 'Es Podeng', 30: 'Es Semangka', 31: 'Es Teh Manis', 32: 'Es Teler', 33: 'Gado-gado', 34: 'Gelato', 35: 'Greek Yoghurt dengan Buah & Granola', 36: 'Ikan Bandeng Goreng', 37: 'Ikan Gurame Asam Manis', 38: 'Jus Alpukat', 39: 'Jus Apel', 40: 'Jus Jeruk', 41: 'Kari Ayam', 42: 'Kentang Goreng', 43: 'Keripik Kentang', 44: 'Kerupuk Udang', 45: 'Klepon', 46: 'Kopi Americano', 47: 'Kopi Latte', 48: 'Kue Apem', 49: 'Kue Bolu Coklat', 50: 'Kue Cubit', 51: 'Kue Lumpur', 52: 'Lapis Legit (1 potong)', 53: 'Lasagna', 54: 'Lumpia Basah', 55: 'Makaroni Keju', 56: 'Martabak Keju', 57: 'Mie Ayam', 58: 'Mie Goreng', 59: 'Mie Kocok', 60: 'Milk Shake', 61: 'Mochi', 62: 'Nagasari', 63: 'Nasi Goreng', 64: 'Nasi Goreng Ayam', 65: 'Nasi Hainan', 66: 'Nasi Merah', 67: 'Nasi Padang', 68: 'Nasi Uduk', 69: 'Nugget Ayam', 70: 'Oatmeal Ubi Jalar', 71: 'Pecel Lele', 72: 'Pempek', 73: 'Perkedel Jagung', 74: 'Perkedel Kentang', 75: 'Pisang Goreng Madu', 76: 'Pizza Keju', 77: 'Puding Coklat', 78: 'Ramen Ayam', 79: 'Rawon', 80: 'Rendang', 81: 'Risol Bihun', 82: 'Risol Mayo', 83: 'Roti Isi Coklat', 84: 'Salad Buah', 85: 'Salmon Panggang', 86: 'Sandwich Keju', 87: 'Sate Ayam', 88: 'Serabi', 89: 'Siomay', 90: 'Soda', 91: 'Sop buah', 92: 'Soto ayam', 93: 'Soto mie', 94: 'Spaghetti', 95: 'Sup ayam', 96: 'Susu coklat', 97: 'Tahu isi', 98: 'Teh tanpa gula', 99: 'Teh tarik', 100: 'Telur dadar sayur', 101: 'Telur goreng', 102: 'Telur rebus', 103: 'Tempe orek', 104: 'Tumis kangkung', 105: 'Tumis tahu', 106: 'Tuna salad sandwich', 107: 'Udang goreng', 108: 'Udang lapis tepung'}
foods = ['Ikan Gurame Asam Manis', 'Salmon Panggang', 'Telur rebus', 'Kari Ayam', 'Udang lapis tepung', 'Perkedel Jagung', 'Sandwich Keju', 'Tahu isi', 'Gado-gado', 'Mie Kocok', 'Klepon', 'Cilok', 'Greek Yoghurt dengan Buah & Granola', 'Telur dadar sayur', 'Ayam (Dilapisi Tepung Roti dan Digoreng)', 'Pempek', 'Kue Apem', 'Es Krim Strawberry', 'Tuna salad sandwich', 'Mie Ayam', 'Kerupuk Udang', 'Telur goreng', 'Kue Bolu Coklat', 'Donat (Glazed)', 'Gelato', 'Bakso Daging Sapi', 'Empal Gentong', 'Nasi Uduk', 'Soto mie', 'Perkedel Kentang', 'Soto ayam', 'Rawon', 'Nasi Goreng Ayam', 'Kue Lumpur', 'Kentang Goreng', 'Udang goreng', 'Nasi Merah', 'Tumis kangkung', 'Belgian Waffle', 'Lasagna', 'Salad Buah', 'Siomay', 'Nasi Goreng', 'Makaroni Keju', 'Nasi Padang', 'Nagasari', 'Sup ayam', 'Serabi', 'Martabak Keju', 'Es Krim Vanila', 'Rendang', 'Risol Bihun', 'Mie Goreng', 'Oatmeal Ubi Jalar', 'Burger', 'Brownies', 'Tempe orek', 'Dimsum', 'Tumis tahu', 'Lapis Legit (1 potong)', 'Es Krim Coklat', 'Nasi Hainan', 'Pisang Goreng Madu', 'Kue Cubit', 'Ramen Ayam', 'Spaghetti', 'Cumi Goreng', 'Chicken Katsu', 'Ayam Geprek', 'Nugget Ayam', 'Keripik Kentang', 'Risol Mayo', 'Ikan Bandeng Goreng', 'Roti Isi Coklat', 'Es Loli', 'Bubur Ayam', 'Mochi', 'Puding Coklat', 'Bakpia', 'Dadar Gulung (2 lapis)', 'Sate Ayam', 'Lumpia Basah', 'Pecel Lele', 'Pizza Keju']
foods = [food.lower().replace(" ", "") for food in foods]
data = {'Nasi Uduk': [1.83, 260.0, 160.0], 'Bubur Ayam': [0.19, 372.0, 240.0], 'Ayam Geprek': [2.34, 789.0, 300.0], 'Nasi Goreng': [1.13, 250.0, 149.0], 'Bakso Daging Sapi': [1.63, 218.0, 108.0], 'Soto Mie': [1.56, 370.0, 300.0], 'Es Teh Manis': [17.15, 68.0, 178.0], 'Es Jeruk peras': [15.62, 84.0, 186.0], 'Es kelapa muda': [23.98, 113.0, 240.0], 'Es Kopi': [6.54, 30.0, 30.0], 'Spaghetti': [0.78, 220.0, 140.0], 'Nasi Goreng Ayam': [1.04, 247.0, 149.0], 'Makaroni Keju': [8.72, 493.0, 243.0], 'Kue Bolu Coklat ': [26.37, 196.0, 66.0], 'Mie Kocok': [2.65, 388.0, 240.0], 'Pizza Keju': [6.12, 475.0, 172.0], 'Kari Ayam': [3.66, 219.0, 177.0], 'Sup Ayam': [0.27, 75.0, 241.0], 'Susu Coklat': [24.02, 190.0, 250.0], 'Jus Apel': [20.27, 87.0, 186.0], 'Ramen Ayam': [2.0, 280.0, 63.0], 'Belgian Waffle': [13.0, 220.0, 65.0], 'Mie Goreng': [6.0, 390.0, 85.0], 'Donat (Glazed)': [13.0, 240.0, 60.0], 'Es Krim Strawberry': [14.71, 125.0, 103.0], 'Kentang Goreng': [0.33, 156.0, 89.0], 'Burger': [6.7, 272.0, 112.0], 'Nugget Ayam': [0.25, 43.0, 19.0], 'Telur Goreng': [0.38, 89.0, 50.0], 'Jus Jeruk': [21.0, 110.0, 240.0], 'Risol Mayo': [0.74, 329.0, 120.0], 'Risol Bihun': [1.24, 187.0, 120.0], 'Soto Ayam ': [0.98, 312.0, 241.0], 'Nasi Merah': [0.35, 110.0, 100.0], 'Kerupuk Udang': [0.12, 151.0, 28.0], 'Perkedel Kentang': [0.13, 107.0, 75.0], 'Telur Rebus': [0.56, 77.0, 50.0], 'Kue Apem': [5.43, 171.0, 90.0], 'Ayam (Dilapisi Tepung Roti dan Digoreng)': [0.88, 190.0, 100.0], 'Martabak Keju': [2.09, 204.0, 80.0], 'Kue Cubit ': [9.34, 141.0, 60.0], 'Es Podeng': [17.77, 188.0, 125.0], 'Es Doger': [17.59, 341.0, 240.0], 'Es Teler': [44.98, 425.0, 240.0], 'Es Loli': [4.81, 27.0, 35.0], 'Brownies': [12.5, 129.0, 34.0], 'Bakpia': [5.62, 149.0, 50.0], 'Keripik Kentang': [1.15, 153.0, 28.0], 'Empal Gentong ': [2.23, 415.0, 250.0], 'Serabi': [4.35, 323.0, 150.0], 'Klepon': [20.0, 120.0, 50.0], 'Dadar Gulung (2 lapis)': [7.0, 200.0, 100.0], 'Nagasari': [15.0, 250.0, 100.0], 'Kue Lumpur': [15.0, 100.0, 50.0], 'Lapis Legit (1 potong)': [20.0, 350.0, 100.0], 'Es Dawet': [10.0, 200.0, 250.0], 'Sop Buah': [15.0, 250.0, 250.0], 'Cendol': [10.0, 200.0, 250.0], 'Es Kacang Merah': [15.0, 150.0, 250.0], 'Es Campur': [15.0, 300.0, 250.0], 'Rendang': [3.14, 468.0, 240.0], 'Gado-gado': [4.43, 318.0, 241.0], 'Siomay': [0.19, 103.0, 75.0], 'Dimsum': [0.48, 94.0, 84.0], 'Sate Ayam': [0.89, 101.0, 45.0], 'Mie Ayam': [1.32, 421.0, 240.0], 'Es Krim Coklat': [33.73, 143.0, 66.0], 'Es Semangka': [12.0, 50.0, 14.0], 'Nasi Padang': [17.76, 664.0, 380.0], 'Pempek': [11.18, 234.0, 120.0], 'Pecel Lele': [9.67, 292.0, 150.0], 'Rawon': [1.07, 288.0, 241.0], 'Ikan Gurame Asam Manis': [2.79, 261.0, 135.0], 'Cilok': [2.91, 319.0, 120.0], 'Kopi Latte': [13.55, 135.0, 408.0], 'Soda': [33.76, 140.0, 369.0], 'Cumi Goreng': [0.56, 106.0, 85.0], 'Ikan Bandeng Goreng': [0.31, 349.0, 150.0], 'Udang Goreng': [0.77, 244.0, 85.0], 'Udang Lapis Tepung ': [3.0, 150.0, 100.0], 'Gelato': [31.62, 124.0, 97.0], 'Perkedel Jagung': [1.15, 91.0, 35.0], 'Tahu Isi': [1.68, 134.0, 120.0], 'Milk Shake': [49.01, 382.0, 283.0], 'Teh Tarik': [20.89, 124.0, 250.0], 'Puding Coklat': [20.17, 157.0, 112.0], 'Pisang Goreng Madu': [28.78, 215.0, 120.0], 'Roti isi Coklat': [13.0, 280.0, 100.0], 'Es Krim Vanila': [10.0, 120.0, 100.0], 'Lumpia Basah': [0.47, 80.0, 64.0], 'Tempe Orek': [5.13, 175.0, 100.0], 'Tuna Salad Sandwich': [6.19, 287.0, 157.0], 'Sandwich Keju': [3.59, 261.0, 83.0], 'Tumis Kangkung': [3.0, 150.0, 200.0], 'Salmon Panggang': [0.17, 250.0, 150.0], 'Sup Sayur Ayam': [3.0, 200.0, 300.0], 'Salad Buah': [10.0, 150.0, 200.0], 'Oatmeal Ubi Jalar': [5.0, 200.0, 250.0], 'Telur Dadar Sayur': [2.0, 200.0, 200.0], 'Tumis Tahu': [2.0, 180.0, 250.0], 'Greek Yoghurt dengan Buah & Granola': [15.0, 300.0, 250.0], 'Jus Alpukat': [12.96, 195.0, 150.0], 'Cappucino': [6.41, 74.0, 249.0], 'Teh Tanpa Gula': [0.0, 0.0, 250.0], 'Air Putih': [0.0, 0.0, 250.0], 'Mochi': [7.12, 224.0, 70.0], 'Kopi Americano': [0.0, 15.0, 473.0], 'Chicken Katsu': [2.0, 240.0, 100.0], 'Lasagna': [2.72, 163.0, 100.0], 'Nasi Hainan': [2.0, 50.0, 14.5]}
data_lower = {key.lower().replace(" ", ""): value for key, value in data.items()}

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
            result_lower = result.lower().replace(" ", "")

            if result_lower in foods:
                st.info('**Category : Foods**')
            else:
                st.info('**Category : Drinks**')
            st.success("**Predicted : " + result + '**')
            st.warning(f'**Sugar {data_lower[result_lower][0]}(gr), Calories {data_lower[result_lower][1]}(Kkal), Serving size per {data_lower[result_lower][2]}(gr)**')


run()