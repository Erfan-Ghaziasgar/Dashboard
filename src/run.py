import streamlit as st

from src.utils import (count_messages, create_bar_chart, create_dataframe,
                       display_dataframe, load_json, set_up, upload_file)


def main():
    set_up()
    uploaded_file = upload_file()
    if uploaded_file is not None:
        json_data = load_json(uploaded_file)
        if 'messages' in json_data:
            df = create_dataframe(json_data)
            display_dataframe(df)
            message_counts = count_messages(df)
            fig = create_bar_chart(message_counts)
            with st.expander("Click to see the bar chart"):
                st.pyplot(fig)
        else:
            st.write("The uploaded JSON file does not have 'messages' field.")


if __name__ == "__main__":
    main()
