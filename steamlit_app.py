import streamlit 
import pandas as pd
import requests
import snowflake.connector 
from urllib.error import URLError
streamlit.title('My Parents healthy DIner') 
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, spinach & Oat smoothie')
streamlit.text('🐔 Hard boiled free range egg')
streamlit.text('🥑 Avacado toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

 
my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list.set_index('Fruit', inplace=True)

#Let's add an option for users to pick the fruits for their own smoothie
fruits_selected = streamlit.multiselect('Pick some fruits : ', list(my_fruit_list.index), ['Avocado','Strawberries']) 
fruits_to_show = my_fruit_list.loc[fruits_selected]
#Display the list of fruits
streamlit.dataframe(fruits_to_show)


#new section for API response
streamlit.header("Fruityvice Fruit Advice!")
try:
 fruit_choice = streamlit.text_input('What fruit would you like information about?')
 if not fruit_choice:
  streamlit.error('Please select a fruit to get information') 
 else:
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)  
  # Load the json response to a dataframe and normalize
  fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
  streamlit.dataframe(fruityvice_normalized)
except URLError as e:
 streamlit.error() 

# Show the parsed json data as a table


streamlit.stop()

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
#streamlit.write("Thanks for adding", add_my_fruit)
my_cur.execute("insert into PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST values ('from streamlit')")
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.text("The fruit load list contains:")
streamlit.dataframe(my_data_rows)
fruit_choice1 = streamlit.text_input('What fruit would you like information about?','Jackfruit')
streamlit.write('The user entered ', fruit_choice1)
fruityvice_response1 = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice1)
streamlit.text(fruityvice_response1.json())
