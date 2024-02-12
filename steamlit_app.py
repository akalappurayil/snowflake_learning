import streamlit
streamlit.title('My Parents healthy DIner') 
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, spinach & Oat smoothie')
streamlit.text('🐔 Hard boiled free range egg')
streamlit.text('🥑 Avacado toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas as pd 
my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
#my_fruit_list.set_index('Fruit')

#Let's add an option for users to pick the fruits for their own smoothie
streamlit.multiselect('Pick some fruits : ', list(my_fruit_list.Fruit)) 
#Display the list of fruits
streamlit.dataframe(my_fruit_list)
