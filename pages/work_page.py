# Run main_page.py first
import streamlit as st
import pandas as pd

# Set the page name
st.sidebar.markdown("# Worksheet Page")

# Load in data, and cache it so we don't have to load in a lot of data on refresh.
@st.cache
def get_data():
    return pd.read_csv("data.csv").drop(['_c0'],axis=1) #use different data here maybe
df = get_data()

# Write a header that says "Learning how to use Streamlit"

st.header("Learning how to use Streamlit: ", anchor=None)

# Create a check box labeled "Show data" that when checked, displays the dataframe

agree = st.checkbox("Show Data", value=False, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False)
if agree == True:
    st.write(df)

# Create a slider that allows the user to choose a range between two years from our movie dataset
x = st.slider('Number of movies to display:', value=(1893,2005), min_value=1950, max_value=2010)
#start_color, end_color = st.select_slider(
#    'Select a range of movie years',
#     options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'],
#     value=('red', 'blue'))
#st.write('You selected wavelengths between', start_color, 'and', end_color)
