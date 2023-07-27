import pandas as pd
import json
import streamlit as st
import matplotlib.pyplot as plt

# create a title for your app with emoji icon. text align to center.
st.title("Streamlit App :sunglasses:")
st.header("Hi :wave: Welcome to Streamlit App")

uploaded_file = st.file_uploader(
    label=":blue_heart: Choose a JSON file", type='json')
if uploaded_file is not None:
    # Load the JSON data
    json_data = json.loads(uploaded_file.getvalue().decode())

    # If messages field is present
    if 'messages' in json_data:
        # Convert messages to pandas DataFrame
        df = pd.json_normalize(json_data['messages'])

        # Display the DataFrame in Streamlit
        st.dataframe(df)

        # Count the number of messages sent by each actor
        message_counts = df['from'].value_counts()

        # Create a bar chart of the number of messages sent by each actor
        fig, ax = plt.subplots()
        message_counts.plot(kind='bar', ax=ax)
        # ax.set_xlabel('Actor')
        # ax.set_ylabel('Number of Messages)
        st.pyplot(fig)
    else:
        st.write("The uploaded JSON file does not have 'messages' field.")
