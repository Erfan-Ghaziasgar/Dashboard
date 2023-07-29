import pandas as pd
import json
import streamlit as st
import matplotlib.pyplot as plt

def set_up():
    # create a title for your app with emoji icon. text align to center.
    st.title("Streamlit App :sunglasses:")
    st.header("Hi :wave: Welcome to Streamlit App")


def upload_file():
    # Upload the JSON file
    uploaded_file = st.file_uploader(
        label=":blue_heart: Choose a JSON file", type='json')
    return uploaded_file

def load_json(uploaded_file):
    # Load the JSON data
    json_data = json.loads(uploaded_file.getvalue().decode())
    return json_data

def create_dataframe(json_data):
    # Convert messages to pandas DataFrame
    df = pd.json_normalize(json_data, record_path='messages')
    return df

def display_dataframe(df):
    # Display the DataFrame in Streamlit
    with st.expander("Click to see the DataFrame"):
        st.dataframe(df)

def count_messages(df):
    # Count the number of messages sent by each actor
    message_counts = df['from'].value_counts()
    return message_counts

def create_bar_chart(message_counts):
    # Create a bar chart of the number of messages sent by each actor
    fig, ax = plt.subplots()
    message_counts.plot(kind='bar', ax=ax)
    return fig

